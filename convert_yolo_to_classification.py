#!/usr/bin/env python3
"""
Converte dataset YOLO detecção para classificação por classe de rosto
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict
import random

# Classes de expressões faciais (9 classes, IDs 0-8)
CLASSES = [
    'angry',      # 0
    'disgust',    # 1
    'fear',       # 2
    'happy',      # 3
    'neutral',    # 4
    'sad',        # 5
    'surprise',   # 6
    'confused',   # 7
    'calm'        # 8
]

def get_class_from_label(label_file):
    """Lê arquivo de label e retorna a classe (primeiro número)"""
    try:
        with open(label_file, 'r') as f:
            first_line = f.readline().strip()
            class_id = int(first_line.split()[0])
            return class_id
    except:
        return None

def convert_to_classification(
    source_dir,
    output_dir="dataset-sample",
    samples_per_class_train=20,
    samples_per_class_val=5,
    seed=42
):
    """
    Reorganiza dataset YOLO para estrutura de classificação
    """
    random.seed(seed)

    source_path = Path(source_dir)
    output_path = Path(output_dir)

    # Encontrar pasta base
    base_folder = None
    for item in source_path.iterdir():
        if item.is_dir() and 'Facial' in item.name:
            base_folder = item
            break

    if not base_folder:
        print(f"❌ Pasta com 'Facial' não encontrada em {source_path}")
        return False

    print(f"✓ Encontrada pasta base: {base_folder.name}")

    # Criar estrutura
    for split in ['train', 'val']:
        for class_name in CLASSES:
            (output_path / split / class_name).mkdir(parents=True, exist_ok=True)

    # Processar train e valid
    for split_name, split_folder_name in [('train', 'train'), ('val', 'valid')]:
        split_path = base_folder / split_folder_name
        images_dir = split_path / 'images'
        labels_dir = split_path / 'labels'

        if not images_dir.exists():
            print(f"⚠️ {split_name} não encontrado")
            continue

        # Agrupar imagens por classe
        class_images = defaultdict(list)

        for label_file in labels_dir.glob('*.txt'):
            class_id = get_class_from_label(label_file)
            if class_id is not None and 0 <= class_id < len(CLASSES):
                # Encontrar imagem correspondente
                img_name = label_file.stem
                img_file = None
                for ext in ['.jpg', '.png', '.jpeg']:
                    candidate = images_dir / (img_name + ext)
                    if candidate.exists():
                        img_file = candidate
                        break

                if img_file:
                    class_images[class_id].append(img_file)

        # Copiar subset balanceado
        limit = samples_per_class_train if split_name == 'train' else samples_per_class_val

        total_copied = 0
        for class_id, img_files in class_images.items():
            class_name = CLASSES[class_id]

            # Embaralhar e limitar
            random.shuffle(img_files)
            selected = img_files[:limit]

            # Copiar
            output_class_dir = output_path / split_name / class_name
            for img_file in selected:
                shutil.copy2(img_file, output_class_dir / img_file.name)

            print(f"  {split_name}/{class_name}: {len(selected)} imagens")
            total_copied += len(selected)

        print()

    # Estatísticas
    print("=" * 60)
    print("✓ Conversão concluída!")
    print("=" * 60)

    total_train = sum(len(list((output_path / 'train' / c).glob('*'))) for c in CLASSES)
    total_val = sum(len(list((output_path / 'val' / c).glob('*'))) for c in CLASSES)

    print(f"📁 Diretório: {output_dir}")
    print(f"📊 Classes: {len(CLASSES)}")
    print(f"📈 Treino: {total_train} imagens")
    print(f"📈 Validação: {total_val} imagens")

    size_gb = sum(f.stat().st_size for f in output_path.rglob('*') if f.is_file()) / (1024**3)
    print(f"💾 Tamanho: {size_gb:.2f} GB")

    return True

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python convert_yolo_to_classification.py <dataset_path>")
        sys.exit(1)

    source = sys.argv[1]
    convert_to_classification(source)
