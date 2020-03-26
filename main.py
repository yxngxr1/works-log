from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def server():
    session = db_session.create_session()
    users = session.query(User).all()
    jobs = session.query(Jobs).all()
    title = 'Works Log'
    return render_template('index.html', title=title, users=users, jobs=jobs)


def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()

    user1 = User(surname="Scott", name="Ridley", age="21", position="captain", speciality="engineer",
                 address="module_1",
                 email="Ridley@mars.org")
    user2 = User(surname="Weir", name="Andy", age="21", position="captain", speciality="engineer",
                 address="module_1",
                 email="Andy@mars.org")
    user3 = User(surname="Sanders", name="Teddy", age="21", position="captain", speciality="engineer",
                 address="module_1",
                 email="Teddy@mars.org")

    for user in [user1, user2, user3]:
        session.add(user)
    session.commit()

    job1 = Jobs(team_leader=1, job='Deployment of residential modules 1 and 2', work_size=15, collaborators='2, 3',
                start_date=(datetime.datetime.now()), is_finished=False, user=user1)
    job2 = Jobs(team_leader=2, job='Exploration of mineral resources', work_size=20, collaborators='4, 3',
                start_date=(datetime.datetime.now()), is_finished=True, user=user2)
    job3 = Jobs(team_leader=3, job='Development of a management system', work_size=25, collaborators='5',
                start_date=(datetime.datetime.now()), is_finished=False, user=user3)

    for job in [job1, job2, job3]:
        session.add(job)
    session.commit()

    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
