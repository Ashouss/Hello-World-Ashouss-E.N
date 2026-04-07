if [ $# -lt 2 ]; then
    echo "Ошибка: нужно 2 аргумента (имя гена и уровень экспрессии)"
    exit 1
fi
gene_name=$1
expression=$2
echo "Экспрессия гена $gene_name составляет $expression единиц"
