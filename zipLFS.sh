#!/bin/bash
# chmod +x zip LFS.sh

# Мінімальний розмір файлу у мегабайтах
MIN_SIZE_MB=50

# Переводимо у байти
MIN_SIZE_BYTES=$((MIN_SIZE_MB * 1024 * 1024))

# Знайти великі zip-файли
large_files=$(find . -type f -name "*.zip" -size +"$MIN_SIZE_BYTES"c)

if [ -z "$large_files" ]; then
    echo "Великих zip-файлів (>${MIN_SIZE_MB}MB) не знайдено."
    exit 0
fi

echo "Знайдено великі файли:"
echo "$large_files"

# Додати їх у Git LFS
for file in $large_files; do
    echo "Додаємо $file у Git LFS..."
    git lfs track "$file"
    git add "$file"
done

# Додати .gitattributes (створений git lfs track)
git add .gitattributes

# Закомітити зміни
git commit -m "Move large zip files to Git LFS"

echo "Файли додані у LFS. Тепер можна пушити:"
echo "git push origin main"
