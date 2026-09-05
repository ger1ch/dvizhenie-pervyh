КАК ОПУБЛИКОВАТЬ НА GITHUB PAGES

1. Создайте новый репозиторий на GitHub, например:
   dvizhenie-pervyh

2. Загрузите в корень репозитория ВСЕ файлы из этой папки:
   index.html
   education.html
   science.html
   ...
   папку assets

3. На GitHub откройте:
   Settings → Pages

4. В разделе Build and deployment:
   Source: Deploy from a branch
   Branch: main
   Folder: /(root)
   Нажмите Save.

5. Через некоторое время GitHub покажет адрес сайта вида:
   https://USERNAME.github.io/dvizhenie-pervyh/

6. Затем запустите файл generate_qr.py на компьютере:
   python generate_qr.py https://USERNAME.github.io/dvizhenie-pervyh/

   После этого появится папка qr_codes с 12 QR-кодами.
