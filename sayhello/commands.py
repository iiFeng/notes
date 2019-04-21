import click
from sayhello import app, db
from sayhello.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop:
        click.confirm('the operation will delete database,do u want to continue?', abort=True)
        db.drop_all()
        click.echo('drop tables')
    db.create_all()
    click.echo('initialized database')


@app.cli.command()
@click.option('--count', default=20, help='Quantity of message,default is 20.')
def forge(count):
    """Generate fake messages"""
    from faker import Faker
    db.drop_all()
    db.create_all()
    fake = Faker()
    click.echo('Working...')
    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('create %d fake messages.' % count)
