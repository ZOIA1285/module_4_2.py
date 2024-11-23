def  test_function():
    def inner_function():
        print(f'Я в области видимости функции test_function')
    inner_function()


test_function() #При выполнении данного кода будет выведено сообщение "Я в области видимости функции test_function" при вызове функции `test_function`
 #Попытка вызвать `inner_function` вне функции `test_function` приводит к ошибке `NameError`



