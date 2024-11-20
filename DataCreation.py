import numpy as np

class DataCreation:
    def __init__(self, seedvalue, numS, numSprime, numeq, numhazar, numper, numV, numDepots,
                 coeff_bounds, h1_bounds, h2_bounds, coord_bounds):
        self.seedvalue = seedvalue
        np.random.seed(self.seedvalue)
        
        # Inputs
        self.numS = numS
        self.numSprime = numSprime
        self.numeq = numeq
        self.numhazar = numhazar
        self.numper = numper
        self.numV = numV
        self.numDepots = numDepots

        # Bounds
        self.coeff_bounds = coeff_bounds  # (lower, upper)
        self.h1_bounds = h1_bounds        # (lower, upper)
        self.h2_bounds = h2_bounds        # (lower, upper)
        self.coord_bounds = coord_bounds  # (lower, upper)

        # Initialize attributes
        self.M = [f'd{i+1}' for i in range(self.numDepots)]  # Dynamically generate depot list
        self.coefficient = None
        self.Kdepo = None
        self.Kdepo_2 = None
        self.s_1 = None
        self.s_2 = None
        self.D = None
        self.f = None
        self.N = None
        self.Nprime = None
        self.K = None
        self.T = None
        self.P = None
        self.Pprime = None
        self.E = None
        self.incident_edges_dict = None
        self.edges_N_Nprime = None
        self.c = None
        self.g = None
        self.d = None
        self.q = None
        self.a = None
        self.b_1 = None
        self.h_1 = None
        self.h_2 = None
        self.l = None
        self.o = None
        self.Tmax = None
        self.tr = None
        self.bmax = None
        self.kappa = None
        self.t_prime = None
        self.coordinates = None

        # Generate data
        self._generate_data()

    def _generate_data(self):
        # Define sets and parameters
        self.N = list(range(1, self.numS + 1))
        self.Nprime = list(range(1001, 1001 + self.numSprime))
        self.K = list(range(1, self.numV + 1))
        self.T = list(range(1, self.numper + 1))
        self.P = list(range(1, self.numeq + 1))
        self.Pprime = list(range(self.numeq + 6, self.numeq + self.numhazar + 6))

        self.Kdepo = {m: [k for k in self.K if (k % self.numDepots) == (i % self.numDepots)] for i, m in enumerate(self.M)}
        self.Kdepo_2 = {k: self.M[k % self.numDepots] for k in self.K}

        # Generate sample-specific data
        self._generate_sample_specific_data()

    def _generate_sample_specific_data(self):
        # Generic coefficient generation
        self.coefficient = {k: np.random.uniform(*self.coeff_bounds) for k in self.K}

        # Generic holding cost generation (h_1 and h_2)
        self.h_1 = {i: {p: np.random.uniform(*self.h1_bounds) for p in self.P} for i in self.N}
        self.h_2 = {i: {p: np.random.uniform(*self.h2_bounds) for p in self.Pprime} for i in self.Nprime}

        # Generic coordinate generation
        self.coordinates = {node: np.random.uniform(*self.coord_bounds, size=2) for node in self.N + self.M}

        # Generate edges
        self._generate_edges()

    def _generate_edges(self):
        # Edges
        self.edges_M_N = [(i, j) for i in self.M for j in self.N]
        self.edges_M_Nprime = [(i, j) for i in self.M for j in self.Nprime]
        self.edges_N_Nprime = [(i, j) for i in self.N for j in self.Nprime]
        self.edges_N = [(i, j) for i in self.N for j in self.N if i < j]
        self.edges_Nprime = [(i, j) for i in self.Nprime for j in self.Nprime if i < j]
        self.E = self.edges_M_N + self.edges_M_Nprime + self.edges_N_Nprime + self.edges_N + self.edges_Nprime

        # Incident edges dictionary
        self.incident_edges_dict = {node: [(i, j) for i, j in self.E if i == node or j == node] for node in self.N + self.Nprime + self.M}




coeff_bounds = (1.2, 1.5)  # Coefficient bounds for omega 
h1_bounds = (6, 10)        # Holding cost h_1 bounds
h2_bounds = (11, 15)       # Holding cost h_2 bounds 
coord_bounds = (0, 500)    # Coordinate bounds

# Create an object using the DataCreation class
data_object = DataCreation(
    seedvalue=42,    # Random seed for reproducibility
    numS=12,         # Number of satellite nodes
    numSprime=8,     # Number of backhauling satellite nodes
    numeq=10,        # Number of equipment types
    numhazar=5,      # Number of hazardous materials
    numper=3,        # Number of periods
    numV=3,          # Number of vehicles
    numDepots=2,     # Number of depots (d1, d2)
    coeff_bounds=coeff_bounds,
    h1_bounds=h1_bounds,
    h2_bounds=h2_bounds,
    coord_bounds=coord_bounds
)