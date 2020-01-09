import os


class HandlePath:
    input_files = []
    processed_path = ''
    output_sub_path = ''
    output_file_path = ''
    output_path = ''

    input_file_path = ''
    path = ''

    def calculate_entropy(self, folder, n, bins):
        sub_folder = 'entropy_' + str(n) + '-' + str(bins)
        self.output_file_path = sub_folder + '.csv'
        self.processed_path = os.path.join('V:\\thesis\\processed_data', folder)
        self.input_files = os.listdir(self.processed_path)
        project_path = os.path.dirname(os.path.dirname(__file__))
        self.output_path = os.path.join(project_path, 'output_data', folder)
        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)
        self.output_sub_path = os.path.join(self.output_path, sub_folder)
        if not os.path.exists(self.output_sub_path):
            os.mkdir(self.output_sub_path)

    def plot_entropy(self, folder, n, bins):
        project_path = os.path.dirname(os.path.dirname(__file__))
        sub_folder = 'entropy_' + str(n) + '-' + str(bins)
        self.path = os.path.join(project_path, 'output_data', folder, sub_folder)
        self.input_file_path = os.path.join(self.path, sub_folder + '.csv')

    def train_dict(self, name, k, d):
        processed_up_path = 'V:\\thesis\\processed_data'
        self.input_file_path = os.path.join(processed_up_path, name + '_byte')
        project_path = os.path.dirname(os.path.dirname(__file__))
        self.output_file_path = os.path.join(project_path, 'output_data', name + '_dict' + '_' + str(k) + '_' + str(d))

    def read_dict(self, name):
        project_path = os.path.dirname(os.path.dirname(__file__))
        self.input_file_path = os.path.join(project_path, 'output_data', name)

