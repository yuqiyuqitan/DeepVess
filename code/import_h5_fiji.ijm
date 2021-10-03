
//file_path="/home/ortegagranilloa/danceParty/DeepVess/hernandez_figure1a.hdf5";
//file_path="/mnt/efs/woods_hole/danceParty/data/processed/testing/hernandez_figure1a.hdf5";
file_path=File.openDialog("Select h5 file");

run("HDF5...", "open="+file_path);
waitForUser("Click ok when done loading XP");
setMinAndMax("-0.50", "0.50");
