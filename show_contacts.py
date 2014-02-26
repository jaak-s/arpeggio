import argparse
import xmlrpclib

host='localhost'
port=9123

# WITH HELP FROM
# `https://bitbucket.org/blundell/credoscript/src/0975daeea0cbd97a298daf471550794941b5aed0/credoscript/pymol.py?at=default`
# `https://bitbucket.org/blundell/credoscript/src/0975daeea0cbd97a298daf471550794941b5aed0/credoscript/support/pymolviewer.py?at=default`
# `https://bitbucket.org/blundell/credoscript/src/0975daeea0cbd97a298daf471550794941b5aed0/credoscript/config-default.json?at=default`

pymol_config = {
    
        "dashcolor":
        {
            "normal": "cyan",
            "disordered_region": "deepsalmon",

            "xbond":
            {
                "vdwclash": "blue",
                "vdw": "tv_blue",
                "proximal": "slate"
            },

            "hbond":
            {
                "vdwclash": "red",
                "vdw": "deepsalmon",
                "proximal": "salmon"
            },

            "weakhbond":
            {
                "vdwclash": "orange",
                "vdw": "amber",
                "proximal": "peach"
            },

            "metalcomplex":
            {
                "covalent": "purple",
                "vdwclash": "purple",
                "vdw": "medium_purple"
            },

            "ionic":
            {
                "vdwclash": "yellow",
                "vdw": "maize",
                "proximal": "cream"
            },

            "aromatic":
            {
                "vdwclash": "cyan",
                "vdw": "electric_blue",
                "proximal": "baby_blue"
            },

            "hydrophobic":
            {
                "vdwclash": "green",
                "vdw": "emerald",
                "proximal": "moss_green"
            },

            "carbonyl":
            {
                "vdwclash": "rose",
                "vdw": "brilliant_rose",
                "proximal": "thulian_pink"
            },

            "undefined":
            {
                "covalent": "white",
                "vdwclash": "grey90",
                "vdw": "grey60",
                "proximal": "grey30"
            }
        },

        "dashradius":
        {
            "normal": 0.02,

            "xbond":
            {
                "vdwclash": 0.12,
                "vdw": 0.08,
                "proximal": 0.04
            },

            "hbond":
            {
                "vdwclash": 0.12,
                "vdw": 0.08,
                "proximal": 0.04
            },

            "weakhbond":
            {
                "vdwclash": 0.12,
                "vdw": 0.08,
                "proximal": 0.04
            },

            "metalcomplex":
            {
                "covalent": 0.16,
                "vdwclash": 0.12,
                "vdw": 0.08
            },

            "ionic":
            {
                "vdwclash": 0.12,
                "vdw": 0.08,
                "proximal": 0.04
            },

            "aromatic":
            {
                "vdwclash": 0.12,
                "vdw": 0.08,
                "proximal": 0.04
            },

            "hydrophobic":
            {
                "vdwclash": 0.12,
                "vdw": 0.08,
                "proximal": 0.04
            },

            "carbonyl":
            {
                "vdwclash": 0.12,
                "vdw": 0.08,
                "proximal": 0.04
            },

            "undefined":
            {
                "covalent": 0.16,
                "vdwclash": 0.12,
                "vdw": 0.08,
                "proximal": 0.04
            }
        },

        "dashgap":
        {
            "normal": 0.0,

            "xbond":
            {
                "vdwclash": 0.25,
                "vdw": 0.35,
                "proximal": 0.45
            },

            "hbond":
            {
                "vdwclash": 0.25,
                "vdw": 0.35,
                "proximal": 0.45
            },

            "weakhbond":
            {
                "vdwclash": 0.25,
                "vdw": 0.35,
                "proximal": 0.45
            },

            "metalcomplex":
            {
                "covalent": 0.20,
                "vdwclash": 0.25,
                "vdw": 0.35
            },

            "ionic":
            {
                "vdwclash": 0.25,
                "vdw": 0.35,
                "proximal": 0.45
            },

            "aromatic":
            {
                "vdwclash": 0.25,
                "vdw": 0.35,
                "proximal": 0.45
            },

            "hydrophobic":
            {
                "vdwclash": 0.25,
                "vdw": 0.35,
                "proximal": 0.45
            },

            "carbonyl":
            {
                "vdwclash": 0.25,
                "vdw": 0.35,
                "proximal": 0.45
            },

            "undefined":
            {
                "covalent": 0.0,
                "vdwclash": 0.25,
                "vdw": 0.35,
                "proximal": 0.45
            }
        },

        "dashlength":
        {
            "normal": 1.0,

            "xbond":
            {
                "vdwclash": 0.08,
                "vdw": 0.06,
                "proximal": 0.04
            },

            "hbond":
            {
                "vdwclash": 0.08,
                "vdw": 0.06,
                "proximal": 0.04
            },

            "weakhbond":
            {
                "vdwclash": 0.08,
                "vdw": 0.06,
                "proximal": 0.04
            },

            "metalcomplex":
            {
                "covalent": 0.10,
                "vdwclash": 0.08,
                "vdw": 0.06
            },

            "ionic":
            {
                "vdwclash": 0.08,
                "vdw": 0.06,
                "proximal": 0.04
            },

            "aromatic":
            {
                "vdwclash": 0.08,
                "vdw": 0.06,
                "proximal": 0.04
            },

            "hydrophobic":
            {
                "vdwclash": 0.08,
                "vdw": 0.06,
                "proximal": 0.04
            },

            "carbonyl":
            {
                "vdwclash": 0.08,
                "vdw": 0.06,
                "proximal": 0.04
            },

            "undefined":
            {
                "covalent": 1.0,
                "vdwclash": 0.08,
                "vdw": 0.06,
                "proximal": 0.04
            }
        },

        "colors":
        {
            "carbon": "grey",
            "non-std-res": "green",
            "variations": "magenta"
        }
}

# MAIN
if __name__ == '__main__':
    
    # ARGUMENT PARSING
    parser = argparse.ArgumentParser(description='''
    
    #############
    # OPENCREDO #
    #############
    
    Interaction Viewer
    
    A program for calculating CREDO interactions,
    using only Open Source dependencies.
    
    Dependencies:
    - Python (v2.7)
    - PyMOL, run as `pymol -R` to enable the XML-RPC server.
    
    **You must have already run your structure with OpenCREDO to generate the required output files**.
    Be careful about absolute and relative paths, this script might not mind but PyMOL probably will.
    
    ''', formatter_class=argparse.RawTextHelpFormatter)
        
    parser.add_argument('pdb', type=str, help='Path to the PDB file to be analysed.')    
    
    args = parser.parse_args()
    
    pdb_filename = args.pdb
    contacts_filename = pdb_filename.replace('.pdb', '.contacts')
    rings_filename = pdb_filename.replace('.pdb', '.rings')
    ari_filename = pdb_filename.replace('.pdb', '.ari') # ATOM-RING INTERACTIONS
    ri_filename = pdb_filename.replace('.pdb', '.ri') # RING-RING INTERACTIONS
    
    srv = xmlrpclib.Server('http://{}:{}'.format(host, port))
    do = srv.do
    
    # PYMOL SETUP
    
    do('reinitialize')

    # SET PYMOL VARIABLES FOR PRETTIER MOLECULES
    do('set valence, 1')
    do('set stick_rad, 0.15')
    do('set line_width, 1')
    do('set mesh_width, 0.3')

    # DECREASE FONT SIZE
    do('set label_size, 10')

    # MAKE SPHERES LOOK PRETTIER (WATER, IONS...')
    do('set sphere_scale, 0.15')

    # DASH PROPERTIES
    do('set dash_round_ends, 0')
    do('set dash_gap, 0.25')
    do('set dash_length, 0.05')

    # COLORS
    do('set_color maize, (251, 236, 93)') # IONIC VDW
    do('set_color cream, (255, 253, 208)') # IONIC PROXIMAL

    do('set_color electric_purple, (191, 0, 255)') # METAL COMPLEX VDW CLASH
    do('set_color medium_purple, (147, 112, 219)') # METAL COMPLEX VDW

    do('set_color amber, (255, 191, 0)')
    do('set_color peach, (255, 229, 180)')

    do('set_color electric_blue, (125, 249, 255)') #
    do('set_color baby_blue, (224, 255, 255)')

    do('set_color emerald, (80, 200, 120)')
    do('set_color moss_green, (173, 200, 173)')

    do('set_color rose, (255, 0, 127)')
    do('set_color brilliant_rose, (246, 83, 166)')
    do('set_color thulian_pink, (222, 111, 161)')

    do('set_color neon_red, (255, 0, 102)')

    # DNA
    do('set cartoon_ladder_mode, 1')
    do('set cartoon_ring_finder, 1')
    do('set cartoon_ring_mode, 3')
    do('set cartoon_nucleic_acid_mode, 4')
    do('set cartoon_ring_transparency, 0.5')
    
    # QUALITY
    do('set line_smooth, 1')
    do('set antialias, 2')
    do('set cartoon_fancy_helices, 1')
    do('set depth_cue, 1')
    do('set specular,1')
    do('set surface_quality, 1')
    do('set stick_quality, 15')
    do('set sphere_quality, 2')
    do('set cartoon_sampling, 14')
    do('set ribbon_sampling, 10')
    do('set transparency_mode, 2')
    do('set stick_ball, 1')
    do('set stick_ball_ratio, 1.5')
    do("rebuild")
    
    # LOAD STRUCTURE
    do('load {}'.format(pdb_filename))
    
    # DEFER UPDATE
    do('set defer_update, 1')
    
    # GET CONTACTS
    with open(contacts_filename, 'rb') as fo:
        
        interactions = []
        used_interaction_types = set([])
        dist_flag = ''
        
        for line in fo:
            
            line = line.strip().split('\t')
            
            atom_bgn = line[0]
            atom_end = line[1]
            SIFt = [int(x) for x in line[2:]]
            
            # `https://bitbucket.org/blundell/credovi/src/bc337b9191518e10009002e3e6cb44819149980a/credovi/structbio/contacts.py?at=default`
            # SIFT:
            # 0: CLASH
            # 1: COVALENT
            # 2: VDW_CLASH
            # 3: VDW
            # 4: PROXIMAL
            # 5: HBOND # 0
            # 6: WEAK_HBOND # 1
            # 7: HALOGEN_BOND # 2
            # 8: IONIC # 3
            # 9: METAL_COMPLEX # 4
            #10: AROMATIC # 5
            #11: HYDROPHOBIC # 6
            #12: CARBONYL # 7
            
            # MUTALLY EXCLUSIVE TYPES
            
            # CLASH
            if SIFt[0]:
                dist_flag = 'clash'
                
                # SKIPPING CLASHES FOR NOW
                continue
                
            # COVALENT
            elif SIFt[1]:
                
                dist_flag = 'covalent'
                
                # SKIPPING COVALENTS FOR NOW
                continue
            
            # VDW_CLASH
            elif SIFt[2]:
                dist_flag = 'vdw_clash'
                
            # VDW
            elif SIFt[3]:
                dist_flag = 'vdw'
                
            # PROXIMAL
            elif SIFt[4]:
                dist_flag = 'proximal'
                
            else:
                dist_flag = 'undefined'
            
            # FEATURE CONTACTS
            
            for e, interaction in enumerate(SIFt[5:]):
                
                interaction_type = ''
                
                if interaction:
                    
                    if e == 0:
                        interaction_type = 'hbond'
                    
                    elif e == 1:
                        interaction_type = 'weakhbond'
                    
                    elif e == 2:
                        interaction_type = 'xbond'
                        
                    elif e == 3:
                        interaction_type = 'ionic'
                        
                    elif e == 4:
                        interaction_type = 'metalcomplex'
                    
                    elif e == 5:
                        interaction_type = 'aromatic'
                    
                    elif e == 6:
                        interaction_type = 'hydrophobic'
                    
                    elif e == 7:
                        interaction_type = 'carbonyl'
                    
                    interactions.append((interaction_type, dist_flag))
            
            for interaction_type, flag in interactions:
                
                do('distance {}-{}, {}, {}'.format(interaction_type, flag, atom_bgn, atom_end))
                used_interaction_types.add((interaction_type, flag))
        
        for interaction_type, flag in used_interaction_types:
            
            label = '{}-{}'.format(interaction_type, flag)
            
            do('color {}, {}'.format(pymol_config[interaction_type][flag], label))
            do('set dash_radius, {}, {}'.format(pymol_config['dashradius'][interaction_type][flag], label))
            do('set dash_gap, {}, {}'.format(pymol_config['dashgap'][interaction_type][flag], label))
            do('set dash_length, {}, {}'.format(pymol_config['dashlength'][interaction_type][flag], label))
    
    do('hide labels')
    
    # UPDATE PYMOL NOW
    do('set defer_update, 0')
        