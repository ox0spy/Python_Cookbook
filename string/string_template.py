#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

form_letter = '''Dear $customer,
I hope you are having a great time.
If you do not find Room $room to your satisfaction,
let us know. Please accept this $$5 coupon.
            Sincerely,
            $manager
            $${name} Inn'''

letter_template = string.Template(form_letter)
print letter_template.substitute({'name': 'Sleepy',
                                  'customer': 'Fred Smith',
                                  'manager': 'Barney Mills',
                                  'room': 307})

print
msg = string.Template('the square of $number is $square')
for i in range(10):
    print msg.substitute(number=i, square=i*i)

# locals()
print
msg = string.Template('the square of $number is $square')
for number in range(10):
    print msg.substitute(locals(), square=number*number)


print
msg = string.Template('an $adj $msg')
adj = 'interesting'
print msg.substitute(locals(), msg='message')
