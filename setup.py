from distutils.core import setup

setup(
    name='CalendarToast',
    version='1.0',
    packages=['CalendarToast'],
    url='https://github.com/abhijeetnigam/CalendarToast.git',
    license='',
    author='Abhijeet Nigam',
    author_email='abhijeet.nigam@Outlook.com',
    install_requires=['win10toast', 'pywin32'],
    description='Toast Notification to inform that meeting is about to end and end user should wrapup his meeting'
)
