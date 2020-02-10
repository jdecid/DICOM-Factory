POSSIBLE_ARGS = [
    'seed',
    'SeriesDescription',
    'Rows',
    'Columns'
]


def validate_kwargs(args):
    for k, v in args.items():
        if k not in POSSIBLE_ARGS:
            raise ValueError('Parameter `%s` with value `%s` is not a supported argument.'.format(k, v))
