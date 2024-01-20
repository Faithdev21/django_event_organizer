from csv import DictReader

from django.core.management import BaseCommand
from django.db import IntegrityError

from chat.models.room import Room
from events.models.event import Event
from events.models.organization import Organization
from users.models import User


class Command(BaseCommand):
    """Load CSV data into database"""
    def handle(self, *args, **kwargs):
        for row in DictReader(open('./data/organizations.csv', encoding='utf-8')):
            try:
                organization = Organization(
                    title=row['title'],
                    description=row['description'],
                    address=row['address'],
                    postcode=row['postcode']
                )
                organization.save()
            except IntegrityError:
                print("Organization with this title already created!")
        print("Organizations ready!")

        for row in DictReader(open('./data/rooms.csv', encoding='utf-8')):
            try:
                room = Room(
                    name=row['name'],
                    slug=row['slug']
                )
                room.save()
            except IntegrityError:
                print("Room with this parameters already created!")
        print("Rooms ready!")

        for row in DictReader(open('./data/users.csv', encoding='utf-8')):
            try:
                user = User(
                    password=row['password'],
                    email=row['email'],
                    phone_number=row['phone_number']
                )
                user.save()
            except IntegrityError:
                print("User with this email already created!")
        print("Users ready!")
