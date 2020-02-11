from django.utils import timezone
import re


years = list(range(timezone.now().year-5, timezone.now().year+6))
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}
days = list(range(1, 32))

# def get_read_time(text):
