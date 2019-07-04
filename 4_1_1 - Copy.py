@pytest.mark.regression
# тест вне класса: отступа нет
def test_student_can_see_lesson_name_in_lesson_in_course_after_joining(self, driver):
    # все строки внутри теста с отступом
    page = CoursePromoPage(url=self.course.url, driver=driver)
    page.open()


class TestLessonNameInCourseForTeacher(object):
    @pytest.mark.regression
    # тест внутри класса, нужен дополнительный отступ
    def test_teacher_can_see_lesson_name_in_lesson_in_course(self, driver):
        # еще один отступ для каждой строки, и так с любым уровнем вложенности
        page = LessonPlayerPage(url=self.lesson_url, driver=driver)
        page.open()
        try:
            # плюс один отступ на каждый уровень вложенности
            dangerous_function()
        except:
            close_something()
			
			
Что такое Page Object Model?			
		Основная идея состоит в том, что каждую страницу веб-приложения 
		можно описать в виде объекта класса. Способы взаимодействия пользователя 
		со страницей можно описать с помощью методов класса. 	
		
 Page Object - это абстрактный объект, который содержит в себе методы для работы 
 с конкретной веб-страницей. 	
 
Важно! Обычно методы у Page Object бывают двух типов: сделать что-то и проверить что-то.		
			
def test_add_to_cart(browser):
    page = ProductPage(url="", browser)   # инициализируем объект Page Object
    page.open()                           # открываем страницу в браузере
    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart()            # жмем кнопку добавить в корзину 
    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом			
			
			
			
			
			
			
			
			
			