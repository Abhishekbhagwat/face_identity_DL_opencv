from preprocess import preprocesses

input_datadir = './train_img'
output_datadir = './pre_img'

obj = preprocesses(input_datadir, output_datadir)
num_images_total, num_successfully_aligned = obj.collect_data()

print('Total number of images: %d' % num_images_total)
print('Number of successfully aligned images: %d' % num_successfully_aligned)
