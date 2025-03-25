GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

PATIENT_TYPE_CHOICES = [
    ('', '-----'),
    ('Member_Patient', 'Member_Patient'),
    ('NextOfKin_Patient', 'NextOfKin_Patient'),
    ('Staff', 'Staff'),
    ('New_Patient', 'New_Patient'),
]

SPECIALIZATION_CHOICES = [
    ('', '----------'),
    ('Dentistry', 'Dentistry'),
    ('Pharmacy', 'Pharmacy'),
    ('Consultation', 'Consultation'),
    ('Laboratory', 'Laboratory Tests'),
    ('Other issue', 'Other issue'), ]

APPOINTMENT_STATUS_CHOICES = (
    ('', '-----'),
    ('Failed', 'Failed'),
    ('Scheduled', 'Scheduled'),
    ('Canceled', 'Canceled'),
    ('Completed', 'Completed'),
)
PAYMENT_CHOICES = [
    (True, 'Verified'),
    (False, 'N/A'), ]

FOR_CHOICES = [
    ('', '-----'),
    ('self', 'Self'),
    ('next_of_kin', 'Next of Kin'),
]
