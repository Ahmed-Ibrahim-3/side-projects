import csv
import numpy as np

rawcc = open(r"C:\Users\ahmed\OneDrive\Documents\co21\CreditCardcheckerV3\example_cc.txt").read().split()

cc_convert = []
for nums in rawcc:
    cc_convert.append(nums.strip())

# Card name constants
AMERICAN_EXPRESS = 'American Express'
DISCOVER = 'Discover'
MASTERCARD = 'MasterCard'
VISA = 'VISA'
BANKCARD = 'Bankcard'
RUPAY = 'RuPay'
DANKORT = 'Dankort'
CHINA_T_UNION = 'China T Union'
CHINA_UNIONPAY = 'China union pay'
UKRCARD = 'Ukrcard'
INTERPAYMENT = 'Interpayment'
INSTAPAYMENT = 'Instapayment'
JCB = 'JCB'
MIR = 'MIR'
NPS_PRIDNESTROVIE = 'NPR Pridnestrovie'
SOLO = 'Solo'
SWITCH = 'Switch'
MAESTRO = 'Maestro'
MAESTRO_UK = 'Maestro UK'
VISA_ELECTRON = 'VISA electron'
TROY = 'Troy'
UATP = 'UATP'
VERVE = 'Verve'
LANKAPAY = 'LankaPay'
UZ = 'UZ'
HUMO = 'Humo'

# Card number constants
AMERICAN_EXPRESS_2 = ('34', '37')
CHINA_T_UNION_2 = ('31')
CHINA_UNIONPAY_2 = ('62')
MASTERCARD_2 = [str(x) for x in range(51, 55)]
MASTERCARD_4 = [str(x) for x in range(2221, 2720)]
DISCOVER_3 = [str(x) for x in range(644, 650)]
DISCOVER_4 = '6011',
DISCOVER_5 = [str(x) for x in range(622126, 622925)]
UKRCARD_4 = ('6040', '6041', '6042')
INTERPAYMENT_3 = '636'
INSTAPAYMENT_3 = ('637', '638', '639')
JCB_4 = [str(x) for x in range(3528, 2589)]
MIR_4 = [str(x) for x in range(2200, 2204)]
NPS_PRIDNESTROVIE_6 = [str(x) for x in range(6054740, 6052744)]
SOLO_4 = [str(x) for x in range(6334, 6767)]
SWITCH_4 = ('4903', '4905', '4911', '4936', '6333', '6759')
SWITCH_6 = ('633110', '564182')
TROY_2 = '65'
TROY_4 = '9792'
VISA_1 = '4'
MAESTRO_4 = ('5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763')
MAESTRO_UK_4 = '6759'
MAESTRO_UK_6 = ('676770', '676774')
VISA_ELECTRON_4 = ('4026', '4508', '4844', '4913', '4917')
VISA_ELECTRON_6 = '417500'
UATP_1 = '1'
VERVE_6 = [str(x) for x in range(506099, 506189)]
VERVE_6.extend([str(x) for x in range(65002, 650027)])
LANKAPAY_6 = '357111'
UZ_4 = '8600'
HUMO_4 = '9860'
BANKARD_2 = '56'
BANKARD_4 = '5620'
BANKARD_6 = [str(x) for x in range(560221, 560225)]
RUPAY_2 = ('60', '65', '81', '82')
RUPAY_3 = ('508', '353', '356')
DANKORT_4 = '5019', '4571'

# test card numbers
test_nums = [
    122000000000003,
    3434343434343,
    5555555555554444,
    5019717010103742,
    36700102000000,
    36148900647913,
    6011000400000000,
    3528000700000000,
    630495060000000000,
    630490017740292441,
    6759649826438453,
    6799990100000000019,
    5555555555554444,
    5454545454545454,
    4444333322221111,
    4911830000000,
    4917610000000000,
    4462030000000000,
    4917610000000000003,
    4917300800000000,
    4484070000000000,
    378282246310005,
    371449635398431,
    378734493671000,
    5610591081018250,
    30569309025904,
    38520000023237,
    6011111111111117,
    6011000990139424,
    3530111333300000,
    3566002020360505,
    5555555555554444,
    5105105105105100,
    4111111111111111,
    4012888888881881,
    4222222222222,
    76009244561,
    5019717010103742,
    6331101999990016,
]


def card_issuer(card_num):
    card_type = ''
    card_num = str(card_num)

    # AMEX
    if len(card_num) == 15 and card_num[:2] in AMERICAN_EXPRESS_2:
        card_type = AMERICAN_EXPRESS_2

    # rest of cards
    elif len(card_num) == 16:

        # MasterCard
        if card_num[:2] in MASTERCARD_2 or card_num[:4] in MASTERCARD_4:
            card_type = MASTERCARD

        # Visa
        elif card_num[:1] in VISA_1:
            card_type = VISA

        # Bankcard
        elif card_num[:2] in BANKARD_2 or card_num[:4] in BANKARD_4 or card_num[:6] in BANKARD_6:
            card_type = BANKCARD

        # China T union
        elif card_num[:2] in CHINA_T_UNION_2:
            card_type = CHINA_T_UNION

        # China Union pay
        elif card_num[:2] in CHINA_UNIONPAY_2:
            card_type = CHINA_UNIONPAY

        # Discover
        elif card_num[:3] in DISCOVER_3 or card_num[:4] in DISCOVER_4 or card_num[:5] in DISCOVER_5:
            card_type = DISCOVER

        # UKRcard
        elif card_num[:4] in UKRCARD_4:
            card_type = UKRCARD

        # Interpayment
        elif card_num[:3] in DISCOVER_3:
            card_type = DISCOVER

        # Instapayment
        elif card_num[:3] in DISCOVER_3:
            card_type = INSTAPAYMENT

        # NPS pridnestrovie
        elif card_num[:6] in NPS_PRIDNESTROVIE_6:
            card_type = NPS_PRIDNESTROVIE

        # SOLO
        elif card_num[:4] in SOLO_4:
            card_type = SOLO

        # Switch
        elif card_num[:4] in SWITCH_4 or card_num[:6] in SWITCH_6:
            card_type = SWITCH

        # Troy
        elif card_num[:2] in TROY_2 or card_num[:4] in TROY_4:
            card_type = TROY

        # Maestro
        elif card_num[:4] in MAESTRO_4:
            card_type = MAESTRO

        # Maestro UK
        elif card_num[:4] in MAESTRO_UK_4 or card_num[:6] in MAESTRO_UK_6:
            card_type = MAESTRO_UK

        # VISA Electron
        elif card_num[:4] in VISA_ELECTRON_4 or card_num[:6] in VISA_ELECTRON_6:
            card_type = VISA

        # UATP
        elif card_num[:1] in UATP_1:
            card_type = UATP

        # Verve
        elif card_num[:6] in VERVE_6:
            card_type = VERVE

        # LankaPay
        elif card_num[:6] in LANKAPAY_6:
            card_type = LANKAPAY

        # UZ
        elif card_num[:4] in UZ_4:
            card_type = UZ

        # HUMO
        elif card_num[:4] in HUMO_4:
            card_type = HUMO

        # RuPay
        elif card_num[:2] in RUPAY_2 or card_num[:3] in RUPAY_3:
            card_type = RUPAY

        # Dankort
        elif card_num[:4] in DANKORT_4:
            card_type = DANKORT

    # VISA
    elif (len(card_num) == 13) and (card_num[:1] in VISA_1):
        card_type = VISA

    return card_type


def digitsum(num):
    return num % 10 + num // 10


def find_check_digit(card_num):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_num)
    org_digit = digits[-1]
    digits.pop()
    even_digits = digits[-1::-2]
    odd_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    even_digits = np.multiply(even_digits, 2)
    even_digits = np.apply_along_axis(digitsum, -1, even_digits)
    checksum += sum(even_digits)
    checkDigit = (10 - (checksum % 10)) % 10
    return ['y' if checkDigit == org_digit else 'n', checkDigit]


def test_check(card_no):
    for i in test_nums:
        if int(card_no) - i == 0:
            is_test = 'y'
            return is_test
        else:
            is_test = 'n'
    return is_test


def full_check(card_no):
    card_info = []
    card_info.append(card_no)
    card_info.extend(find_check_digit(card_no))
    card_info.append(card_issuer(card_no))
    card_info.append(test_check(card_no))
    return card_info


with open("C:/Users/ahmed/OneDrive/Documents/co21/CreditCardcheckerV2/results2.csv", mode='w',
          newline="") as csv_file:  #

    write = csv.writer(csv_file)
    details = ["ccNumber", "Validity", "checkDigit", "issuer", "testCard"]
    write.writerow(details)
    for card in cc_convert:
        write.writerow(full_check(card))

print(full_check(5297500601008568))
