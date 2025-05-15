from django.core.management.base import BaseCommand
from uniapp.models import University

class Command(BaseCommand):
    help = 'Populates the database with sample universities'

    def handle(self, *args, **kwargs):
        # Clear existing universities
        University.objects.all().delete()

        universities = [
            {
                'name': 'University of Science and Technology of Southern Philippines',
                'description': 'USTP is a state university known for its excellence in science, technology, and engineering education. Located in the heart of Cagayan de Oro City, it offers cutting-edge programs and research opportunities.',
                'city': 'cagayan_de_oro',
                'course_level': 'undergraduate',
                'field_of_study': 'engineering',
                'image_url': '/static/images/USTP.png'
            },
            {
                'name': 'Xavier University',
                'description': 'Xavier University - Ateneo de Cagayan is a prestigious private university offering comprehensive education rooted in Jesuit traditions. Known for its strong programs in various fields.',
                'city': 'cagayan_de_oro',
                'course_level': 'postgraduate',
                'field_of_study': 'business',
                'image_url': '/static/images/Xavier.png'
            },
            {
                'name': 'Liceo de Cagayan University',
                'description': 'A leading private university in Northern Mindanao, offering quality education across multiple disciplines. Known for its strong medical and allied health programs.',
                'city': 'cagayan_de_oro',
                'course_level': 'undergraduate',
                'field_of_study': 'medicine',
                'image_url': '/static/images/Liceo.png'
            },
            {
                'name': 'Cagayan de Oro College',
                'description': 'A respected institution offering diverse academic programs with a focus on practical skills and industry readiness. Strong emphasis on technology and business education.',
                'city': 'cagayan_de_oro',
                'course_level': 'undergraduate',
                'field_of_study': 'computer_science',
                'image_url': '/static/images/Cagayan de Oro College.png'
            },
            {
                'name': 'Capitol University',
                'description': 'Known for its quality education and modern facilities, Capitol University offers a wide range of programs with particular strength in healthcare and business studies.',
                'city': 'cagayan_de_oro',
                'course_level': 'postgraduate',
                'field_of_study': 'medicine',
                'image_url': '/static/images/Capitol.png'
            },
            {
                'name': 'Lourdes College',
                'description': 'A Catholic institution committed to holistic education, combining academic excellence with strong values formation. Notable for its education and arts programs.',
                'city': 'cagayan_de_oro',
                'course_level': 'undergraduate',
                'field_of_study': 'arts',
                'image_url': '/static/images/Lourdes.png'
            },
            {
                'name': 'Southern Philippines College',
                'description': 'A progressive institution focused on providing accessible quality education. Offers diverse programs with emphasis on practical skills and industry partnerships.',
                'city': 'cagayan_de_oro',
                'course_level': 'undergraduate',
                'field_of_study': 'business',
                'image_url': '/static/images/SPC.png'
            },
        ]

        for uni_data in universities:
            University.objects.create(**uni_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully added {uni_data["name"]}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated universities')) 