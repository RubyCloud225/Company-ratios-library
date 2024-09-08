import pandas as pd
import numpy as np
from DCF import DCFModel

class SensitivityAnalysis:
    def __init__(self, dcf):
        self.dcf = dcf
        self.base_case_inputs = self.dcf.get_base_case_inputs()
        self.sensitivity_ranges = self.dcf.get_senstivity_ranges()
    
    def perform_sensitivity_analysis(self):
        #perform analysis
        sensitivity_results = np.zeros((len(self.sensitivity_ranges[0]), len(self.sensitivity_ranges[1]), len(self.sensitivity_ranges[2])))
        for i, fcf_per_share in enumerate(self.sensitivity_ranges[0]):
            for j, wacc in enumerate(self.sensitivity_ranges[1]):
                for k, terminal_growth_rate in enumerate(self.sensitivity_ranges[2]):
                    Intrinsic_value = fcf_per_share / (wacc - terminal_growth_rate)
                    sensitivity_results[i, j, k] = Intrinsic_value
        return sensitivity_results
    
    def create_sensitivity_df(self, sensitivity_results):
        sensitivity_df = pd.DataFrame(sensitivity_results.reshape(-1, 1),
                                        columns = ['Intrinsic Value'],
                                        index=pd.MultiIndex.from_prduct([self.sensitivity_range[0],
                                                                        self.sensitivity_range[1],
                                                                        self.sensitivity_range[2]],
                                                                        names=['FCF/Share', 'WACC', 'Terminal Growth Rate']))
        return sensitivity_df
    
class DCF:
    def __init__(self):
        self.DCFModel = DCFModel()
        self.fcf_per_share = self.DCFModel.calculate_fcf() / self.DCFModel.equity
        self.wacc = self.DCFModel.calculate_wacc()
        self.terminal_growth_rate = self.DCFModel.calculate_terminal_value()  # Assume a terminal growth rate of 3%

    def get_base_case_inputs(self):
        return [self.fcf_per_share, self.wacc, self.terminal_growth_rate]

    def get_sensitivity_ranges(self):
        # Define sensitivity ranges
        fcf_per_share_range = [9.0, 10.0, 11.0]
        wacc_range = [0.07, 0.08, 0.09]
        terminal_growth_rate_range = [0.02, 0.03, 0.04]
        return [fcf_per_share_range, wacc_range, terminal_growth_rate_range]

"""
# Usage
dcf = DCF()
sensitivity_analysis = SensitivityAnalysis(dcf)
sensitivity_results = sensitivity_analysis.perform_sensitivity_analysis()
sensitivity_df = sensitivity_analysis.create_sensitivity_df(sensitivity_results)
print(sensitivity_df)

"""
