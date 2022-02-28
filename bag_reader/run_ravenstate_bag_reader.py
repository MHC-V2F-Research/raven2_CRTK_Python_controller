import func_raven_bag_reader as reader


bag_name = 'recorder_ravenstate3.bag'
result_name = bag_name[:-3] + 'csv'

bag_path = 'bag_files'
result_path = 'result_files'


reader.read_bag_ravenstate(bag_name = bag_path + '/' + bag_name, 
                           output_name = result_path + '/' + result_name)