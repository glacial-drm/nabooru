Currently literally justa dumping ground for design decisions
Will be updated eventually...........

    # options
        # store loose files
        # store files within their directory in db (directory based collections)
            # no benefit, we use tags based search
                # makes stuff easier to track?
                # 
            # to what extent
                # is each subdir a new table?
                    # surely we can string manip to get all files in some directory after the fact, hence store loose files
                    # it's a tag based search as well, we'd prefer to store all data in one table rather than iterate over each for simplicity's sake