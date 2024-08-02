
#ifndef  RECONSTRUCTEDPARTICLE_ANALYZERS_H
#define  RECONSTRUCTEDPARTICLE_ANALYZERS_H

#include <cmath>
#include <vector>

#include "TLorentzVector.h"
#include "ROOT/RVec.hxx"
#include "edm4hep/ReconstructedParticleData.h"
#include "edm4hep/ParticleIDData.h"
#include "fastjet/PseudoJet.hh"

namespace FCCAnalyses{

  


namespace ReconstructedParticle{


  //gives the angle between two tlv 
  float get_angle_general(const TLorentzVector &tlv1, const TLorentzVector &tlv2);

  //gives the angle between first jet and missing tlv and second jet and missing tlv => better to use get_angle_general directly
  ROOT::VecOps::RVec<float> get_angle(const TLorentzVector &missing_tlv, const ROOT::VecOps::RVec<float> &e, const ROOT::VecOps::RVec<float> &px, const ROOT::VecOps::RVec<float> &py, const ROOT::VecOps::RVec<float> &pz);



  //sums the two tlv of jets from Durham kt (N=2 as no need for a resobuilder)
  TLorentzVector jetsum(const ROOT::VecOps::RVec<float> &e, const ROOT::VecOps::RVec<float> &px, const ROOT::VecOps::RVec<float> &py, const ROOT::VecOps::RVec<float> &pz); 


  //structure in output of resoantikt
  struct resoantiktstruc {
    //method1 : Z1 (on-shell) = 1+2+ everything different from 3 and 4
    TLorentzVector Z1;
    //still method1 : Z2 (off-shell) = 3+4
    TLorentzVector Z2;
    //method 2 : Z1 = 1 + 2
    TLorentzVector Z1_1_2; 
    //method 3 : Z1 = 1+2+ every jet closer to 1 or 2 than to 3 or 4 (3 and 4 are for the off-shell)
    TLorentzVector Z1_reco;
  };

  //function reconstructing the Zs with the jets from Durham anti-kt 
  
  resoantiktstruc resoantikt(const ROOT::VecOps::RVec<float> &e, const ROOT::VecOps::RVec<float> &px, const ROOT::VecOps::RVec<float> &py, const ROOT::VecOps::RVec<float> &pz, int Njets5, const ROOT::VecOps::RVec<float> &theta);

  //counts the number of jets above a certain energy threshold
  int countNjets(const ROOT::VecOps::RVec<float> &energy, float threshold);
  
  //structure in ouptput of myresoBuilder
  struct resostructure {
    //tlv of the dijet pair reconstructed as the one with mjj closest to mZ
    TLorentzVector Z1;
    //tlv of the dijet pair left
    TLorentzVector Z2;
    //vector containing in first and second entries the flavors of the two jets of the Z1
    ROOT::VecOps::RVec<int> flav1;
    //vector containing in first and second entries the flavors of the two jets of the Z2
    ROOT::VecOps::RVec<int> flav2;
    //vector containing in first and second entries the etas of the two jets of the Z1
    ROOT::VecOps::RVec<float> etaZ1;
    //vector containing in first and second entries the etas of the two jets of the Z2
    ROOT::VecOps::RVec<float> etaZ2;
    ROOT::VecOps::RVec<float> angulardiff;
    ROOT::VecOps::RVec<int> jetmember;
  };



  // 
  resostructure myresoBuilder(const ROOT::VecOps::RVec<float> &e, const ROOT::VecOps::RVec<float> &px, const ROOT::VecOps::RVec<float> &py, const ROOT::VecOps::RVec<float> &pz, const ROOT::VecOps::RVec<float> &flavour, const ROOT::VecOps::RVec<float> &flavourgm, const ROOT::VecOps::RVec<float> &eta_jets, const ROOT::VecOps::RVec<float> &theta, const ROOT::VecOps::RVec<float> &phi);
 
 
  struct sameflavour {
    sameflavour();
    ROOT::VecOps::RVec<float> operator() (float part1, float part2, float part3, float part4);
  };

  struct mass_order {
    float mass; 
    mass_order(float arg_mass);
    ROOT::VecOps::RVec<TLorentzVector> operator() (ROOT::VecOps::RVec<float> m, ROOT::VecOps::RVec<float> px, ROOT::VecOps::RVec<float> py, ROOT::VecOps::RVec<float> pz, ROOT::VecOps::RVec<float> e );
  };


  /// build the resonance from 2 particles from an arbitrary list of input ReconstructedPartilces. Keep the closest to the mass given as input
  struct resonanceBuilder {
    float m_resonance_mass;
    resonanceBuilder(float arg_resonance_mass);
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> operator()(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> legs);
  };

 

  //ROOT::VecOps::RVec<bool> findZleptons(const ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>& legs);
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> findZleptons(const ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>& legs);



  /// build the resonance from N particles from an arbitrary list of input PseudoJets.
  /// Keep the closest to the mass given as input (strategy=1) or use the first 2 jets (strategy=2) or return all combinations (strategy=3)
  struct multijetResonanceBuilder {
    float m_resonance_mass;
    int m_nlegs;
    int m_strategy;
    multijetResonanceBuilder(float arg_resonance_mass, int nlegs=2, int strategy=1);
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> operator()(const ROOT::VecOps::RVec<fastjet::PseudoJet>& legs);
  };


  /// build the recoil from an arbitrary list of input ReconstructedPartilces and the center of mass energy
  struct recoilBuilder {
    recoilBuilder(float arg_sqrts);
    float m_sqrts = 240.0;
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) ;
  };

  /// return the angular separations (min / max / average) between a collection of particles
  struct angular_separationBuilder {
    angular_separationBuilder( int arg_delta); //  0, 1, 2 = max, min, average
    int m_delta = 0;
    float operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) ;
  };


  /// select ReconstructedParticles with transverse momentum greater than a minimum value [GeV]
  struct sel_pt {
    sel_pt(float arg_min_pt);
    float m_min_pt = 1.; //> transverse momentum threshold [GeV]
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);
  };


  //_________________________________________________________
  
 
  struct sel_mass {
    sel_mass(float arg_min_mass, float arg_max_mass = 1e10);
    float m_min_mass = 1.; //> [GeV]
    float m_max_mass = 1e10; //< [GeV]
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);
  };
  
  struct sel_recoil_mass {
    sel_recoil_mass(float arg_min_recoil_mass, float arg_max_recoil_mass = 1e10);
    float m_min_recoil_mass = 1.; //> [GeV]
    float m_max_recoil_mass = 1e10; //< [GeV]
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);
  };

  ROOT::VecOps::RVec<float> get_recoil_mass(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  //Returns ReconstructedParticle. Input: ReconstructedParticle
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> sel_recoilMassCloserToH(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> x, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> y);

  //Returns one ReconstructedParticle. Input: one ReconstructedParticle
  edm4hep::ReconstructedParticleData sel_recoilMassCloserToH(edm4hep::ReconstructedParticleData p, edm4hep::ReconstructedParticleData q);

  //Returns one ReconstructedParticle. Input: one ReconstructedParticle
  edm4hep::ReconstructedParticleData sel_recoilMassFurtherFromH(edm4hep::ReconstructedParticleData p, edm4hep::ReconstructedParticleData q);

  TLorentzVector set_tlvXYZM(const ROOT::VecOps::RVec<float> &px, const ROOT::VecOps::RVec<float> &py, const ROOT::VecOps::RVec<float> &pz, float m);
 

  //_________________________________________________________

  /// select ReconstructedParticles with absolute pseudorapidity less than a maximum absolute value
  struct sel_eta {
    sel_eta(float arg_min_eta);
    float m_min_eta = 2.5; //> pseudorapidity threshold
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);
  };

  /// select ReconstructedParticles with momentum greater than a minimum value [GeV]
  struct sel_p {
    sel_p(float arg_min_p, float arg_max_p = 1e10);
    float m_min_p = 1.; //> momentum threshold [GeV]
    float m_max_p = 1e10; //< momentum threshold [GeV]
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);
  };

  /// select ReconstructedParticles with charge equal or in asolute value
  struct sel_charge {
    sel_charge(int arg_charge, bool arg_abs);
    float m_charge; //> charge condition
    bool  m_abs;//> absolute value of the charge
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);
  };

  /// select a list of reconstructed particles depending on the angle cosTheta axis
  struct sel_axis{
    bool m_pos = 0; //> Which hemisphere to select, false/0=cosTheta<0 true/1=cosTheta>0
    sel_axis(bool arg_pos);
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> operator()(ROOT::VecOps::RVec<float> angle, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);
  };

  /// select a list of reconstructed particles depending on the status of a certain boolean flag
  struct sel_tag {
    bool m_pass; // if pass is true, select tagged jets. Otherwise select anti-tagged ones
    sel_tag(bool arg_pass);
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  operator() (ROOT::VecOps::RVec<bool> tags, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);
  };




  /// return reconstructed particles
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> get(ROOT::VecOps::RVec<int> index, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the transverse momenta of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_pt(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the momenta of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_p(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the momenta of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_px(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the momenta of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_py(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the momenta of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_pz(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the pseudo-rapidity of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_eta(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the rapidity of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_y(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the theta of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_theta(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the phi of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_phi(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the energy of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_e(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the masses of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_mass(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the charges of the input ReconstructedParticles
  ROOT::VecOps::RVec<float> get_charge(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the type of the input ReconstructedParticles
  ROOT::VecOps::RVec<int> get_type(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the TlorentzVector of the input ReconstructedParticles
  ROOT::VecOps::RVec<TLorentzVector> get_tlv(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return the TlorentzVector of the indexed input ReconstructedParticles
  TLorentzVector get_tlv(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in, int index);

  /// return the TlorentzVector of the one input ReconstructedParticle
  TLorentzVector get_tlv(edm4hep::ReconstructedParticleData in);

	/// return visible 4-momentum vector
  TLorentzVector get_P4vis(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// return a 4-momentum vector
  TLorentzVector get_tlv_easy(float e, float px, float py, float pz);

  /// concatenate both input vectors and return the resulting vector
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> merge(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> x, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> y);

  /// remove elements of vector y from vector x
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> remove( ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> x, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> y);

  /// return the size of the input collection
  int get_n(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in);

  /// returns the bjet flavour
  ROOT::VecOps::RVec<bool> getJet_btag(ROOT::VecOps::RVec<int> index, ROOT::VecOps::RVec<edm4hep::ParticleIDData> pid, ROOT::VecOps::RVec<float> values);

  /// get number of b-jets
  int getJet_ntags(ROOT::VecOps::RVec<bool> in);

}//end NS ReconstructedParticle

}//end NS FCCAnalyses
#endif
