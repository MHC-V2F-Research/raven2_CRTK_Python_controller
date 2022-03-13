import func_raven_bag_reader as reader


bag_name = 'recorder_CRTKmeasurejs.bag'
result_name = bag_name[:-3] + 'csv'

bag_path = '/home/holyoke/raven2_CRTK_Python_controller/bag_reader/rosbags'
result_path = '/home/holyoke/raven2_CRTK_Python_controller/bag_reader/rosbags'


reader.read_bag_CRTK_measured_js(bag_name = bag_path + '/' + bag_name, 
                           output_name = result_path + '/' + result_name)
