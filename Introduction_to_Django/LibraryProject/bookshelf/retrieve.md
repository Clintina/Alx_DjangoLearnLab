>>> book = Book.objects.get(title="1984")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\clint\Alx_DjangoLearnLab\.env\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\clint\Alx_DjangoLearnLab\.env\Lib\site-packages\django\db\models\query.py", line 636, in get
    raise self.model.MultipleObjectsReturned(
    ...<5 lines>...
    )
bookshelf.models.Book.MultipleObjectsReturned: get() returned more than one Book -- it returned 2!   
>>> print(book.title, book.author, book.publication_year)
1984 George Orwell 1949