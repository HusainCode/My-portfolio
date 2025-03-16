from flask import Flask, render_template

app = Flask(__name__)


def get_projects():
    return [
        {
            'name': 'Threat Detection URL Checker',
            'url': 'https://github.com/HusainCode/Threat-Detection-URL-Checker',
            'description': 'A tool that checks URLs for potential security threats.'
        },
        {
            'name': 'Simple GoLang Calculator',
            'url': 'https://github.com/HusainCode/simple-calculator',
            'description': 'The calculator can perform basic arithmetic operations including addition, subtraction, multiplication, and division.'
        },
        {
            'name': 'Rock-Paper-Scissors with C',
            'url': 'https://github.com/HusainCode/Rock-Paper-Scissors',
            'description': 'A Rock, Paper, Scissors game implemented in C.'
        }
    ]


def get_social_links():
    return {
        'github': 'https://github.com/HusainCode',
        'linkedin': 'https://www.linkedin.com/in/husain-alshaikhahmed-a6892617b',
        'hackerrank': 'https://www.hackerrank.com/profile/HusainCode',
        'youtube': 'https://www.youtube.com/@HusainCodes'
    }


def get_tech_books():
    return [
        {
            'title': 'Clean Code',
            'author': 'Robert C. Martin',
            'description': 'A handbook of agile software craftsmanship that has helped me write more maintainable code.',
            'rating': 5
        },
        {
            'title': 'Python Crash Course',
            'author': 'Eric Matthes',
            'description': 'A hands-on, project-based introduction to programming with Python.',
            'rating': 4
        },
        {
            'title': 'Effective C++',
            'author': 'Scott Meyers',
            'description': '55 specific ways to improve your programs and designs in C++.',
            'rating': 5
        }
    ]


def get_self_dev_books():
    return [
        {
            'title': 'Atomic Habits',
            'author': 'James Clear',
            'description': 'Tiny changes, remarkable results: how small habits can transform your life.',
            'rating': 5
        },
        {
            'title': 'Deep Work',
            'author': 'Cal Newport',
            'description': 'Rules for focused success in a distracted world.',
            'rating': 4
        },
        {
            'title': 'Mindset',
            'author': 'Carol S. Dweck',
            'description': 'The new psychology of success and how we can learn to fulfill our potential.',
            'rating': 4
        }
    ]


def get_other_books():
    return [
        {
            'title': 'The Pragmatic Programmer',
            'author': 'Andrew Hunt & David Thomas',
            'description': 'From journeyman to master - a guide to the programming craft.',
            'rating': 5
        },
        {
            'title': 'The Design of Everyday Things',
            'author': 'Don Norman',
            'description': 'A powerful primer on how and why some products satisfy customers while others frustrate them.',
            'rating': 4
        }
    ]


def get_testimonials():
    return [
        {
            'text': '"His drive and passion for the field were evident in everything he did, whether it was tackling challenging coding assignments or helping other students understand complex concepts. Husain\'s commitment to learning and personal growth was truly impressive."',
            'author': 'Rodolfo J. Galván Martínez',
            'position': 'Professor at Texas State University'
        },
        {
            'text': '"What truly sets Husain apart is his kindness and willingness to support others. Throughout our time working together, he consistently showed genuine concern for his colleagues\' success and was always ready to lend a helping hand when needed."',
            'author': 'Sameera Raza',
            'position': 'Software Engineer'
        },
        {
            'text': '"What truly sets Husain apart is his dedication to continuous learning and professional development. He actively seeks out opportunities to expand his knowledge base and improve his skills, whether through formal education, online courses, or personal projects."',
            'author': 'Calvin Scharf',
            'position': 'Project Lead'
        },
        {
            'text': '"Husain exhibited reliability, professionalism, and a strong work ethic throughout our collaboration. He was always punctual, prepared, and fully engaged in our projects, demonstrating a level of dedication that is rare to find."',
            'author': 'Faith Goddard',
            'position': 'Team Manager'
        },
        {
            'text': '"He consistently goes above and beyond to ensure project success, and his collaborative spirit makes him a joy to work with. Husain\'s ability to understand complex requirements and translate them into effective solutions is truly remarkable."',
            'author': 'Mustafa Al Tuhaifa',
            'position': 'Technical Lead'
        },
        {
            'text': '"He continuously goes above and beyond to ensure that his assignments are completed to the highest quality. His attention to detail, technical skills, and problem-solving abilities make him an invaluable asset to any team."',
            'author': 'Ivy Doan',
            'position': 'Senior Developer'
        },
        {
            'text': '"I wholeheartedly recommend Husain Alshaikhahmed for any position or endeavor he chooses to pursue. His combination of technical expertise, interpersonal skills, and unwavering work ethic make him an exceptional candidate who will undoubtedly excel in any environment."',
            'author': 'Stephen Johnson',
            'position': 'CTO'
        },
        {
            'text': '"His ability to deescalate stressful situations and remain calm and pleasant is impressive. Husain\'s emotional intelligence and communication skills allow him to effectively collaborate with diverse teams and stakeholders."',
            'author': 'Janel Laya',
            'position': 'Product Manager'
        },
        {
            'text': '"One of Husain\'s notable strengths is his commitment to customer service. He approaches every interaction with genuine care and dedication, ensuring that client needs are not just met, but exceeded."',
            'author': 'Dimitr Dimitrov',
            'position': 'Client Relations Manager'
        },
        {
            'text': '"I\'ve always put a premium on resourcefulness and readiness among my team members and Husain never failed to deliver. His ability to adapt quickly to new challenges and find innovative solutions consistently impressed me throughout our work together."',
            'author': 'Aroofa Mohammad',
            'position': 'Engineering Director'
        }
    ]


def get_udemy_courses():
    return [
        {
            'title': 'Complete Python Bootcamp: From Zero to Hero in Python',
            'instructor': 'Jose Portilla',
            'description': 'Learn Python like a professional! Start from the basics and go all the way to creating your own applications and games!',
            'skills': ['Python fundamentals', 'Object-Oriented Programming', 'Web scraping', 'Data analysis'],
            'completion_date': 'March 2023',
            'url': 'https://www.udemy.com/course/complete-python-bootcamp/'
        },
        {
            'title': 'The Complete Web Developer Course 2.0',
            'instructor': 'Rob Percival, Dr. Angela Yu',
            'description': 'Learn Web Development by building 25 websites and mobile apps using HTML, CSS, Javascript, PHP, Python, MySQL & more!',
            'skills': ['HTML5', 'CSS3', 'JavaScript', 'PHP', 'Python', 'MySQL'],
            'completion_date': 'June 2023',
            'url': 'https://www.udemy.com/course/the-complete-web-developer-course-2/'
        },
        {
            'title': 'Machine Learning A-Z™: Hands-On Python & R In Data Science',
            'instructor': 'Kirill Eremenko, Hadelin de Ponteves',
            'description': 'Learn to create Machine Learning Algorithms in Python and R from two Data Science experts.',
            'skills': ['Data Preprocessing', 'Regression', 'Classification', 'Clustering', 'Deep Learning'],
            'completion_date': 'September 2023',
            'url': 'https://www.udemy.com/course/machinelearning/'
        },
        {
            'title': 'The Complete JavaScript Course 2023: From Zero to Expert!',
            'instructor': 'Jonas Schmedtmann',
            'description': 'The modern JavaScript course for everyone! Master JavaScript with projects, challenges and theory.',
            'skills': ['JavaScript fundamentals', 'DOM manipulation', 'Asynchronous JavaScript', 'Modern JS (ES6+)'],
            'completion_date': 'December 2023',
            'url': 'https://www.udemy.com/course/the-complete-javascript-course/'
        },
        {
            'title': 'React - The Complete Guide (incl Hooks, React Router, Redux)',
            'instructor': 'Maximilian Schwarzmüller',
            'description': 'Dive in and learn React.js from scratch! Learn Reactjs, Hooks, Redux, React Routing, Animations, Next.js and more!',
            'skills': ['React.js', 'Hooks', 'Redux', 'React Router', 'Next.js'],
            'completion_date': 'January 2024',
            'url': 'https://www.udemy.com/course/react-the-complete-guide-incl-redux/'
        },
        {
            'title': 'SQL - MySQL for Data Analytics and Business Intelligence',
            'instructor': '365 Careers',
            'description': 'Learn how to use SQL for data analysis and business intelligence with real-world examples.',
            'skills': ['SQL basics', 'Database design', 'Data analysis', 'Business intelligence'],
            'completion_date': 'November 2023',
            'url': 'https://www.udemy.com/course/sql-mysql-for-data-analytics-and-business-intelligence/'
        }
    ]


def get_other_courses():
    return [
        {
            'title': 'Google Data Analytics Professional Certificate',
            'provider': 'Google (Coursera)',
            'description': 'Prepared for a career in the high-growth field of data analytics with this comprehensive program.',
            'skills': ['Data analysis', 'SQL', 'R programming', 'Data visualization', 'Tableau'],
            'completion_date': 'February 2024',
            'url': 'https://www.coursera.org/professional-certificates/google-data-analytics'
        },
        {
            'title': 'AWS Cloud Practitioner Essentials',
            'provider': 'Amazon Web Services',
            'description': 'Foundational knowledge of cloud computing concepts and AWS services, security, architecture, pricing, and support.',
            'skills': ['AWS', 'Cloud computing', 'Security', 'Architecture'],
            'completion_date': 'October 2023',
            'url': '#'
        },
        {
            'title': 'CS50: Introduction to Computer Science',
            'provider': 'Harvard University (edX)',
            'description': 'An introduction to the intellectual enterprises of computer science and the art of programming.',
            'skills': ['C', 'Python', 'SQL', 'Data structures', 'Algorithms'],
            'completion_date': 'August 2023',
            'url': 'https://www.edx.org/course/introduction-computer-science-harvardx-cs50x'
        }
    ]


@app.route('/')
def home():
    projects = get_projects()
    social_links = get_social_links()

    return render_template('index.html', projects=projects, social_links=social_links)


@app.route('/books')
def books():
    projects = get_projects()  # For the navbar
    tech_books = get_tech_books()
    self_dev_books = get_self_dev_books()
    other_books = get_other_books()

    return render_template('books.html',
                           projects=projects,
                           tech_books=tech_books,
                           self_dev_books=self_dev_books,
                           other_books=other_books)


@app.route('/testimonials')
def testimonials():
    projects = get_projects()  # For the navbar
    all_testimonials = get_testimonials()

    return render_template('testimonials.html',
                           projects=projects,
                           testimonials=all_testimonials)


@app.route('/courses')
def courses():
    projects = get_projects()  # For the navbar
    udemy_courses = get_udemy_courses()
    other_courses = get_other_courses()

    return render_template('courses.html',
                           projects=projects,
                           udemy_courses=udemy_courses,
                           other_courses=other_courses)


if __name__ == '__main__':
    app.run(debug=True)