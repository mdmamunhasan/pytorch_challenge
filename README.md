# We will download the required data files

    !wget -cq https://github.com/udacity/pytorch_challenge/raw/master/cat_to_name.json
    !wget -cq https://s3.amazonaws.com/content.udacity-data.com/courses/nd188/flower_data.zip
    !rm -r flower_data || true
    !unzip -qq flower_data.zip