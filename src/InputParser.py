import argparse


class InputParser(object):

    @staticmethod
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def string_to_boolean(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    @staticmethod
    def string_to_int(v):
        if isinstance(v, int):
            return v
        if InputParser.is_int(v):
            return int(v)
        raise argparse.ArgumentTypeError('Integer value expected.')
