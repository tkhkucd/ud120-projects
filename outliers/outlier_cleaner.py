#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    i=0
    ### your code goes here
    #print("ORIGINAL DATA ++++++++")
    for age in ages:
        #print("age:",age,"net_worths:",net_worths[i],"prediction:",predictions[i])
        #cleaned_data[i]=(age,net_worths[i], abs(net_worths[i]-predictions[i]))
        cleaned_data.append((age,net_worths[i], abs(net_worths[i]-predictions[i])))
        #print("clea_data",i,":",clea_data[i])
        i+=1

    print("CLEARED DATA +++++++++")
    cleaned_data.sort(key=lambda pred_err: pred_err[2])
    #for data in cleaned_data:
    #    print("cleared data :", data )

    print("cleaned_data len:", len(cleaned_data))
    del cleaned_data[int(len(cleaned_data)*0.9):len(cleaned_data)]
    print("cleaned_data len:", len(cleaned_data))

    return cleaned_data
