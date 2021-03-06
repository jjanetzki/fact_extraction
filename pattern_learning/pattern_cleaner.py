from tqdm import tqdm
from storing_tools import PatternTool
from pattern_extraction import Pattern
import os

dir_path = os.path.dirname(os.path.abspath(__file__)) + '/'


class PatternCleaner(PatternTool):
    def __init__(self, least_threshold_types, least_threshold_words,
                 patterns_input_path=dir_path + '../data/patterns_raw.pkl',
                 patterns_output_path=dir_path + '../data/patterns_cleaned.pkl'):
        super(PatternCleaner, self).__init__(patterns_input_path, patterns_output_path)
        self.least_threshold_types = least_threshold_types
        self.least_threshold_words = least_threshold_words

    @classmethod
    def from_config_file(cls):
        config_parser = cls.get_config_parser()
        section = 'pattern_cleaner'
        least_threshold_types = config_parser.getfloat(section, 'least_threshold_types')
        least_threshold_words = config_parser.getfloat(section, 'least_threshold_words')
        return cls(least_threshold_types, least_threshold_words)

    def clean_patterns(self):
        self.logger.print_info('Pattern cleaning...')
        for relation, pattern in tqdm(self.relation_type_patterns.iteritems()):
            self.relation_type_patterns[relation] = Pattern.clean_pattern(pattern,
                                                                          self.least_threshold_words,
                                                                          self.least_threshold_types)
        self.relation_type_patterns = dict(
            filter(lambda (rel, pat): pat is not None, self.relation_type_patterns.iteritems()))
        self.logger.print_done('Pattern cleaning completed.')


if __name__ == '__main__':
    pattern_cleaner = PatternCleaner.from_config_file()
    pattern_cleaner.clean_patterns()
    pattern_cleaner.save_patterns()
