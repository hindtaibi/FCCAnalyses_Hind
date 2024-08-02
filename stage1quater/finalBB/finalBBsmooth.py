import ROOT
import sys

def smooth_histograms(file_list, hist_name, smooth_times):
    for file_name in file_list:
        # Open the ROOT file
        file = ROOT.TFile.Open(file_name, "UPDATE")
        if not file or file.IsZombie():
            print(f"Error opening file {file_name}")
            continue

        # Get the histogram
        hist = file.Get(hist_name)
        if not hist:
            print(f"Histogram {hist_name} not found in file {file_name}")
            file.Close()
            continue

        # Smooth the histogram
        for _ in range(smooth_times):
            hist.Smooth()

        # Save the histogram back to the file
        file.cd()
        hist.Write(hist.GetName(), ROOT.TObject.kOverwrite)

        # Close the file
        file.Close()

# Example usage
if __name__ == "__main__":
    # List of ROOT files
    files = ["outputs/p8_ee_ZZ_ecm240_region2_histo.root"]

    # Name of the histogram to smooth
    histogram_name = "ZZ_m_fit"

    # Number of times to smooth the histogram
    num_smooth_times = 2

    smooth_histograms(files, histogram_name, num_smooth_times)
