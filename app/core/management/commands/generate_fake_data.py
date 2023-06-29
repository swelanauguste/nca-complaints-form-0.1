import random

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Complaint


class Command(BaseCommand):
    help = "Add faker data to the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "count", type=int, help="Number of fake complaints to create"
        )

    def handle(self, *args, **options):
        count = options["count"]
        fake = Faker()
        complaints = []
        for _ in range(count):
            summary = fake.sentence(nb_words=20)
            id_number = fake.ssn()
            name = fake.name()
            email = fake.simple_profile()["mail"]
            address = fake.simple_profile()["address"]
            occupation = fake.profile()["job"]
            phone = fake.msisdn()[:-4]
            phone1 = fake.msisdn()[:-4]
            business_name = fake.company()
            business_address = fake.simple_profile()["address"]
            contact_person = fake.name()
            business_phone = fake.msisdn()[:-4]
            business_email = fake.simple_profile()["mail"]
            model_serial_number = fake.sbn9()
            date_purchased = fake.date_this_month()
            brand = fake.profile()["company"]
            brand_code = fake.random_number(digits=8)
            invoice_receipt_bill = fake.random_number(digits=13)
            manufactured_date = fake.date_this_month()
            complaint = fake.paragraph(nb_sentences=9)
            i_agree = random.randint(0, 1)
            complaint = Complaint(
                summary=summary,
                id_number=id_number,
                name=name,
                email=email,
                address=address,
                occupation=occupation,
                phone=phone,
                phone1=phone1,
                business_name=business_name,
                business_address=business_address,
                contact_person=contact_person,
                business_phone=business_phone,
                business_email=business_email,
                model_serial_number=model_serial_number,
                date_purchased=date_purchased,
                brand=brand,
                brand_code=brand_code,
                invoice_receipt_bill=invoice_receipt_bill,
                manufactured_date=manufactured_date,
                complaint=complaint,
                i_agree=i_agree,
            )
            complaints.append(complaint)
        Complaint.objects.bulk_create(complaints)
        self.stdout.write(self.style.SUCCESS("Data generated"))
