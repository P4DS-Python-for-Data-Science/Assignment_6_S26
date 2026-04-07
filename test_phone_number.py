# Vicente Edited This, Too
from PhoneNumber import *
import pytest

def test_init_():
    '''
    test that creating a new phone number works
    '''
    home = PhoneNumber('4122552626')

def test_911():
    '''
    test that an exception is raised if a phone number begins with 911
    should raise InvalidPhoneNumber exception
    '''
    with pytest.raises(InvalidPhoneNumber) as e_info:
        work = PhoneNumber('9112682565')


def test_valid():
    '''
    tests the is_valid function with numbers that should be created correctly
    (no exceptions raised, is_valid should return true)
    note that valid numbers include 10-digit numbers like
    4122682303
    and 11-digit numbers with a leading 1
    14122682303
    there should NOT be punctuation in the inputs, because the punctuation is 
    removed by the function which calls in_valid, so the input should be a 
    string of digits
    '''
    assert(PhoneNumber.is_valid('1727546317'))
    assert(PhoneNumber.is_valid('17275463317'))

def test_invalid():
    '''
    tests the is_valid function with numbers that should be not be created 
    so it should return false (but does not raise an exception)
    invalid numbers can be
    * too short (<10 digits)
    * too long (>11 digits)
    * 11 digits but the leading digit is a not a 1

    there should NOT be punctuation in the inputs, because the punctuation is 
    removed by the function which calls in_valid, so the input should be a 
    string of digits
    '''
    assert(~PhoneNumber.is_valid('2'))
    assert(~PhoneNumber.is_valid('727256317'))
    assert(~PhoneNumber.is_valid('25702546371'))
    assert(~PhoneNumber.is_valid('717123456789'))

def test_invalid_prefix_code():
    '''
    If the phone number starts with a restricted code, expansion or set-aside code, it should not pass.
    https://www.nationalnanpa.com/area_codes/index.html
    '''
    for n in [2,3,4,5,6,7,8,9]:
        invalid_prefix = f'{n}11'
        test_string = invalid_prefix + '1234567'
        assert(~PhoneNumber.is_valid(test_string))

    for n in [2,3,4,5,6,7,8,9]:
        for x in [0,1,2,3,4,5,6,7,8,9]:
            expansion_code = f'{n}9{x}'
            test_string = expansion_code + '1234567'
            assert(~PhoneNumber.is_valid(test_string))

    for prefix in [37,96]:
        for x in [0,1,2,3,4,5,6,7,8,9]:
            set_aside_code = f'{prefix}{x}'
            test_string = set_aside_code + '1234567'
            assert(~PhoneNumber.is_valid(test_string))


def test_short_numbers():
    ''' 
    test function that tests if a number is invalid:
    if it is too short
    if it is too long '''
    for number_length in range(0,9):
        with pytest.raises(InvalidPhoneNumber) as e_info:
            test_number = PhoneNumber('3'*number_length)

def test_long_numbers():
    ''' 
    test function that tests if a number is invalid:
    if it is too short
    if it is too long '''
    for number_length in range(11,15):
        with pytest.raises(InvalidPhoneNumber) as e_info:
            test_number = PhoneNumber('3'*number_length)
            
def test_service_code():
    '''
    if a phone number starts with services codes  
    N11 
    where N is a digit between 2-9
    it should raise an error
    https://www.nationalnanpa.com/area_codes/index.html
    '''
    for invalid_prefix in ['211','311','411','511',
                           '611','711','811','911']:
        test_string = invalid_prefix + '123 4567'
        with pytest.raises(InvalidPhoneNumber) as e_info:
            test_number = PhoneNumber(test_string)

def test_get_formatted_number():
    ''' creates a number and tests that the number
    is formatted correctly by get_formatted_number 
    '''
    home = PhoneNumber('4122552626')
    assert(home.get_formatted_number() == '(412) 255-2626')

def test_str():
    ''' 
    test that get_formatted_number and (str) methods return the same string
    and that that string is correctly formatted
    don't compare them to each other, but instead create a reference number
    test that when you format it, you get what you expected
    test that when you use str() applied to that object, you again get what you expected
    '''
    temp = PhoneNumber('123) 456-7890')
    assert(temp.get_formatted_number()=='(123) 456-7890')
    assert(str(temp)=='(123) 456-7890')

def test_comparison():
    '''
    test the comparison operators were implemented correctly
    you need to test >,<, <=, >=, and !=

    for comparison purposes, the phone numbers (strings) are compared by value and the order 
    of strings and numbers are the same
    so 222 222 2222 < 555 555 5555 for example

    '''
    twos_number = PhoneNumber('222 222 2222')
    fives_number = PhoneNumber('555 555 5555')
    assert(fives_number>twos_number)
    assert(twos_number<fives_number)
    assert(twos_number<=fives_number)
    assert(fives_number>=twos_number)
    assert(fives_number!=twos_number)

def test_equality():
    '''
    test the equality operators were implemented correctly
    you need to test ==, <=, >=
    make sure to create two different objects, not just compare the object to itself
    so you should create two PhoneNumber objects, and compare them
    for comparison purposes, the phone numbers (strings) are compared by value and the order 
    of strings and numbers are the same
    so 222 222 2222 < 555 555 5555 for example

    '''
    twos_number = PhoneNumber('222 222 2222')
    twos_number_but_different_object = PhoneNumber('222 222 2222')
    assert(repr(twos_number)!=repr(twos_number_but_different_object))
    assert(twos_number==twos_number)
    assert(twos_number==twos_number_but_different_object)
    assert(twos_number_but_different_object>=twos_number)
    assert(twos_number_but_different_object<=twos_number)

def test_set_raw_valid():
    '''
    test_set_raw tests that setting the value of the number with set_raw_number works 
    '''
    test_number = PhoneNumber('222 222 2222')
    test_number.set_raw_number('555 555 5555')
    assert(test_number.get_raw_number()=='5555555555')

def test_getter_methods():
    ''' 
    test that the methods to get parts of a number 
    get_exchange - should get the second three digits of a 10 digit number
    get_area_code - should get the first three digits of a 10 digit number
    get_subscriber_number - should retrieve the last four digits of a 10 digit number
    '''
    home = PhoneNumber('412 123 4567')
    assert(home.get_exchange()=='123')
    assert(home.get_subscriber_number()=='4567')
    assert(home.get_area_code() == '412')

def test_setter_methods_valid_inputs():
    '''
    tests setter methods, with valid inputs
    if you create a valid phone number, test that the correct parts are modified
    and no exceptions are raised, using
    set_area_code
    set_exchange
    set_subscriber_number
    '''
    test_set_num = PhoneNumber()
    assert(test_set_num.get_exchange()=='000')
    assert(test_set_num.get_subscriber_number()=='0000')
    assert(test_set_num.get_area_code()=='000')
    test_set_num.set_area_code('123')
    test_set_num.set_exchange('456')
    test_set_num.set_subscriber_number('7890')
    assert(test_set_num.get_area_code()=='123')
    assert(test_set_num.get_exchange()=='456')
    assert(test_set_num.get_subscriber_number()=='7890')

def test_setter_methods_invalid_inputs():
    '''
    tests setter methods, with invalid inputs
    if you create an invalid phone number, an exception should be raised
    set_area_code
    set_exchange
    set_subscriber_number
    '''
    test_set_num = PhoneNumber()
    assert(test_set_num.get_exchange()=='000')
    assert(test_set_num.get_subscriber_number()=='0000')
    assert(test_set_num.get_area_code()=='000')
    with pytest.raises(InvalidPhoneNumber) as e_info:
        test_set_num.set_area_code('211')
    with pytest.raises(InvalidPhoneNumber) as e_info:
        test_set_num.set_area_code('911')
    with pytest.raises(InvalidPhoneNumber) as e_info:
        test_set_num.set_area_code('23')
    with pytest.raises(InvalidPhoneNumber) as e_info:
        test_set_num.set_exchange('46')
    with pytest.raises(InvalidPhoneNumber) as e_info:
        test_set_num.set_subscriber_number('790')

def test_set_raw_number():
    ''' 
    tests that set_raw_number raises an exception if the input is not the correct length
    or contains an invalid area code, or otherwise is not a valid number
    '''
    temp=PhoneNumber()
    with pytest.raises(InvalidPhoneNumber) as e_info:
        temp.set_raw_number('22')
    with pytest.raises(InvalidPhoneNumber) as e_info:
        temp.set_raw_number('9111234567')

