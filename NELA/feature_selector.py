import os
import csv
import warnings
warnings.filterwarnings("ignore")

DEFAULT_PATH = os.path.dirname(__file__)

def load_features_selected(name):
    with open(os.path.join(DEFAULT_PATH, "resources", "features_selected_"+name+".csv")) as data:
        return [d.replace(" ", "") for d in data.readline().strip().split(",")]

def load_top_features(communities):
    top = []
    for community in communities:
        with open(os.path.join(DEFAULT_PATH, "resources", "top_features_"+community+".csv")) as data:
            top.append((community, data.readline().strip().split(",")))
    return top

def feature_select(path):
    #print "Got to feature selection"
    features_for_fake = load_features_selected("fake")
    features_for_bias = load_features_selected("bias")

    #read in big feature file
    featuresfile = os.path.join(path, "all_features.csv")
    with open(featuresfile) as allfeats:
        feat_names = allfeats.readline().strip().split(",")

        #fake
        if features_for_fake == 'all':
            feats_to_keep_fake = feat_names
        else:
            feats_to_keep_fake = [f for f in feat_names if f in features_for_fake]
        ind_to_keep_fake = [feat_names.index(fk) for fk in feats_to_keep_fake]
        
        #bias
        if features_for_bias == 'all':
            feats_to_keep_bias= feat_names
        else:
            feats_to_keep_bias = [f for f in feat_names if f in features_for_bias]
        ind_to_keep_bias = [feat_names.index(fk) for fk in feats_to_keep_bias]

        for line in allfeats:
            line_to_keep_fake = []
            line_to_keep_consp = []
            line_to_keep_bias = []
            line_to_keep_esist = []
            line_to_keep_newright = []
            line = line.strip().split(",")
            for i in range(len(line)):
                if i in ind_to_keep_fake:
                    line_to_keep_fake.append(line[i])
                
                if i in ind_to_keep_bias:
                    line_to_keep_bias.append(line[i])
            with open(os.path.join(path, "fake_features.csv"), "w") as out:
                out.write(",".join(feats_to_keep_fake)+"\n")
                out.write(",".join(line_to_keep_fake)+"\n")
            
            with open(os.path.join(path, "bias_features.csv"), "w") as out:
                out.write(",".join(feats_to_keep_bias)+"\n")
                out.write(",".join(line_to_keep_bias)+"\n")
            
        #return top_features
            
