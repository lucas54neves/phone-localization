import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

text = input('Enter the phone: ')

for phone in phonenumbers.PhoneNumberMatcher(text, 'BR'):
  formated_phone = phone.number

  phone_location = geocoder.description_for_number(formated_phone, 'pt-br')

  phone_provider = carrier.name_for_number(formated_phone, 'pt-br')

  formated_phone_to_brazil = phonenumbers.format_number(formated_phone, phonenumbers.PhoneNumberFormat.NATIONAL)

  print()

  print('Phone: {}'.format(formated_phone_to_brazil))

  print('Location: {}'.format(phone_location))

  print('Provider: {}'.format(phone_provider))