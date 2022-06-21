# downloaded from https://raw.githubusercontent.com/TadasBaltrusaitis/OpenFace/master/lib/local/LandmarkDetector/model/pdms/In-the-wild_aligned_PDM_68.txt

import pickle
import pathlib

THIS_FILE_PATH = pathlib.Path(__file__)
MODEL_FILE_PATH = pathlib.Path.joinpath(THIS_FILE_PATH.parent, "face_model.bin")

with open(MODEL_FILE_PATH, "rb") as f:
    model_points = pickle.load(f)
