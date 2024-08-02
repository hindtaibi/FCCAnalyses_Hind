#include "FCCAnalyses/ReconstructedParticle.h"
#include <iostream>
#include <cmath>

namespace FCCAnalyses{

namespace ReconstructedParticle{


  float get_angle_general(const TLorentzVector &tlv1, const TLorentzVector &tlv2) {
    float dot = tlv1.Px() * tlv2.Px() + tlv1.Py() * tlv2.Py() + tlv1.Pz() * tlv2.Pz();
    float lenSq1 = tlv1.Px() * tlv1.Px() + tlv1.Py() * tlv1.Py() + tlv1.Pz() * tlv1.Pz();
    float lenSq2 = tlv2.Px() * tlv2.Px() + tlv2.Py() * tlv2.Py() + tlv2.Pz() * tlv2.Pz();
    float norm = std::sqrt(lenSq1*lenSq2);
    float angle = std::acos(dot/norm); 
    return angle;
  }

  ROOT::VecOps::RVec<float> get_angle(const TLorentzVector &missing_tlv, const ROOT::VecOps::RVec<float> &e, const ROOT::VecOps::RVec<float> &px, const ROOT::VecOps::RVec<float> &py, const ROOT::VecOps::RVec<float> &pz) {
     ROOT::VecOps::RVec<float> angle;
    TLorentzVector jet1; 
    TLorentzVector jet2;
    jet1.SetPxPyPzE(px[0], py[0], pz[0], e[0]);
    jet2.SetPxPyPzE(px[1], py[1], pz[1], e[1]);
    
    float dot1 = missing_tlv.Px() * jet1.Px() + missing_tlv.Py() * jet1.Py() + missing_tlv.Pz() * jet1.Pz();
    float dot2 = missing_tlv.Px() * jet2.Px() + missing_tlv.Py() * jet2.Py() + missing_tlv.Pz() * jet2.Pz();
    float lenSqM = missing_tlv.Px() * missing_tlv.Px() + missing_tlv.Py() * missing_tlv.Py() + missing_tlv.Pz() * missing_tlv.Pz();
    float lenSq1 = jet1.Px() * jet1.Px() + jet1.Py() * jet1.Py() + jet1.Pz() * jet1.Pz();
    float lenSq2 = jet2.Px() * jet2.Px() + jet2.Py() * jet2.Py() + jet2.Pz() * jet2.Pz();

    float norm1 = std::sqrt(lenSqM*lenSq1);
    float norm2 = std::sqrt(lenSqM*lenSq2);

    float angle1 = std::acos(dot1/norm1); 
    float angle2 = std::acos(dot2/norm2);

    angle.push_back(angle1); 
    angle.push_back(angle2); 

    return angle;
  }

    
    

 

  TLorentzVector jetsum(const ROOT::VecOps::RVec<float> &e, const ROOT::VecOps::RVec<float> &px, const ROOT::VecOps::RVec<float> &py, const ROOT::VecOps::RVec<float> &pz) {
    TLorentzVector zoffshell;
    zoffshell.SetPxPyPzE(px[0]+px[1], py[0]+py[1], pz[0]+pz[1], e[0]+e[1]);
    return zoffshell;
  }

  resoantiktstruc resoantikt(const ROOT::VecOps::RVec<float> &e, const ROOT::VecOps::RVec<float> &px, const ROOT::VecOps::RVec<float> &py, const ROOT::VecOps::RVec<float> &pz, int Njets5, const ROOT::VecOps::RVec<float> &theta) {
    resoantiktstruc result;
    float PX{0};
    float PY{0};
    float PZ{0};
    float E{0};
    float PXX = px[0] + px[1];
    float PYY = py[0] + py[1];
    float PZZ = pz[0] + pz[1];
    float EE = e[0] + e[1];
    if (Njets5 > 3) {
      result.Z2.SetPxPyPzE(px[2]+px[3], py[2]+py[3], pz[2]+pz[3], e[2]+e[3]);
      result.Z1_1_2.SetPxPyPzE(px[0]+px[1], py[0]+py[1], pz[0]+pz[1], e[0]+e[1]);
      for (int i = 0 ; i<std::size(e); i++) {
	if (i != 2 && i != 3) {
	  PX = PX + px[i];
	  PY = PY + py[i];
	  PZ = PZ + pz[i];
	  E = E + e[i];
	}
      } 
      for (int j = 4 ; j<std::size(e) ; j++) {
	
	float dot1 = px[0] * px[j] + py[0] * py[j] + pz[0] * pz[j];
	float dot2 = px[1] * px[j] + py[1] * py[j] + pz[1] * pz[j];
	float dot3 = px[2] * px[j] + py[2] * py[j] + pz[2] * pz[j];
	float dot4 = px[3] * px[j] + py[3] * py[j] + pz[3] * pz[j];

	float lenSq1 = px[0]*px[0] + py[0]*py[0] + pz[0]*pz[0];
	float lenSq2 = px[1]*px[1] + py[1]*py[1] + pz[1]*pz[1];
	float lenSq3 = px[2]*px[2] + py[2]*py[2] + pz[2]*pz[2];
	float lenSq4 = px[3]*px[3] + py[3]*py[3] + pz[3]*pz[3];
	float lenSqj = px[j]*px[j] + py[j]*py[j] + pz[j]*pz[j];

	float norm1 = std::sqrt(lenSq1*lenSqj);
	float norm2 = std::sqrt(lenSq2*lenSqj);
	float norm3 = std::sqrt(lenSq3*lenSqj);
	float norm4 = std::sqrt(lenSq4*lenSqj);

	float angle1 = std::acos(dot1/norm1);
	float angle2 = std::acos(dot2/norm2);
	float angle3 = std::acos(dot3/norm3);
	float angle4 = std::acos(dot4/norm4);


	
 
	if (abs(angle1) < abs(angle3) || abs(angle1) < abs(angle4) || abs(angle2) < abs(angle3) || abs(angle2) < abs(angle4)) {
	  PXX = PXX + px[j];
	  PYY = PYY + py[j];
	  PZZ = PZZ + pz[j];
	  EE = EE + e[j];
	}
      }
    }
    result.Z1.SetPxPyPzE(PX, PY, PZ, E);
    result.Z1_reco.SetPxPyPzE(PXX,PYY,PZZ,EE); 
    return result;
  }
      

  int countNjets(const ROOT::VecOps::RVec<float> &energy, float threshold) {
    int Njets{0};
    for (int i=0;  i<std::size(energy); i++) {
	    if (energy[i] > threshold) {
	      Njets++; 
	    } 
    }
    return Njets; 
  }
    
  

   resostructure myresoBuilder(const ROOT::VecOps::RVec<float> &e, const ROOT::VecOps::RVec<float> &px, const ROOT::VecOps::RVec<float> &py, const ROOT::VecOps::RVec<float> &pz, const ROOT::VecOps::RVec<float> &flavour, const ROOT::VecOps::RVec<float> &flavourgm, const ROOT::VecOps::RVec<float> &eta_jets, const ROOT::VecOps::RVec<float> &theta, const ROOT::VecOps::RVec<float> &phi) {
    resostructure result;
  int n = e.size();
  float m_1 = 0;
  float newm = 0;
  float m_resonance_mass = 91;
  int a = 0;
  int b = 0;
  int c;
  int d;
  result.flav1.push_back(0);
  result.flav1.push_back(0);
  result.flav1.push_back(0);
  result.flav1.push_back(0);
  result.etaZ1.push_back(0);
  result.etaZ1.push_back(0);
  result.jetmember.push_back(0);
  result.jetmember.push_back(0);
  result.angulardiff.push_back(0);
  result.angulardiff.push_back(0);
  float abstheta{0};
  float mintheta = 200;
  float secondmintheta = 200;
  int ind1 = 0;
  int ind2 = 0;


  ROOT::VecOps::RVec<int> indices;
  for (int i=0;  i<n; i++) {
    indices.push_back(i);
    for (int j=i+1; j<n ; j++) {
      abstheta = abs(theta[i] - theta[j]);
      if (abstheta < mintheta) {
	mintheta = abstheta;
	ind1 = i;
	ind2 = j;
      }
      m_1 = std::sqrt(-(px[i]+px[j])*(px[i]+px[j]) - (py[i]+py[j])*(py[i]+py[j]) - (pz[i]+pz[j])*(pz[i]+pz[j]) + (e[i]+e[j])*(e[i]+e[j]));
      if (abs(m_resonance_mass - newm)  > abs( m_resonance_mass - m_1)) {
	  newm = m_1;
	  float PX = px[i] + px[j];
	  float PY = py[i] + py[j];
	  float PZ = pz[i] + pz[j];
	  result.Z1.SetXYZM(PX, PY, PZ, newm);
	  a = i;
	  b = j;
	  result.flav1[0] = flavour[i];
	  result.flav1[1] = flavour[j];
	  result.flav1[2] = flavourgm[i];
	  result.flav1[3] = flavourgm[j];
	  result.etaZ1[0] = eta_jets[i];
	  result.etaZ1[1] = eta_jets[j];
	  result.jetmember[0] = i+1; //number of the first jet of on shell Z
	  result.jetmember[1] = j+1; //index of the second jet of on shell Z
	  result.angulardiff[0] = abs(theta[i] - theta[j]);
	  result.angulardiff[1] = abs(phi[i] - phi[j]);
	    
      }
    }
  }
  
  for (int k = 0; k<n; k++) {
    for (int l = 0; l<n; l++) {
      abstheta = abs(theta[k] - theta[l]);
      if (k==ind1 && l==ind2) {
	continue;
      } 
      if (abstheta < secondmintheta) {
	secondmintheta = abstheta; 
      }
    }
  }
  
  for (int p=0; p<n; p++) {
    if ( indices[p]!= a && indices[p] !=b  ) {
      c = indices[p];
      break;
    } 
  }
  for ( int q=0; q<n; q++) {
    if (indices[q] != a && indices[q] != b && indices[q] != c) {
      d = indices[q];
    }
  }
  
  float PX = px[c] + px[d];
  float PY = py[c] + py[d];
  float PZ = pz[c] + pz[d];
  result.Z2.SetPxPyPzE(PX, PY, PZ, e[c] + e[d]);
  result.flav2.push_back(flavour[c]);
  result.flav2.push_back(flavour[d]);
  result.flav2.push_back(flavourgm[c]);
  result.flav2.push_back(flavourgm[d]);
  result.etaZ2.push_back(eta_jets[c]);
  result.etaZ2.push_back(eta_jets[d]);
  result.jetmember.push_back(c+1);
  result.jetmember.push_back(d+1);
  result.angulardiff.push_back(abs(theta[c] - theta[d]));
  result.angulardiff.push_back(abs(phi[c] - phi[d]));
  result.angulardiff.push_back(mintheta); //[4] is the minimal theta difference between jets
  result.angulardiff.push_back(secondmintheta); //[5] is the second minimal theta diff between jets
  
			    

  return result;

}

  /*
    sameflavour defines a vector of two floats, the first [0] one associated to the Z on shell and the second [1] one to the Z off shell
    The float takes the value 2 if the two jets in the final state of the Z have the same flavour (determined by get_flavour), 0 otherwise. 
  */ 

 sameflavour::sameflavour() {};
  //part1 and part2 are the flavours of the 2 jets selected as the final state of Z on shell ; same for part3 and part4 for the off shell one
  ROOT::VecOps::RVec<float> sameflavour::operator() (float part1, float part2, float part3, float part4) {
  ROOT::VecOps::RVec<float> flavour;
  int f1;
  int f2;
  if ( abs (part1) == abs(part2) ) {
    f1 = 2; 
  }
  else {
    f1 = 0;
  }
  if ( abs(part3) == abs (part4) ) {
    f2 = 2;
  }
  else {
    f2 = 0; 
  }
  flavour.push_back(f1);
  flavour.push_back(f2);
  return flavour;
    }
    
  /* 
     mass order takes as input the float vector containing the masses of the two jets from Duhram N=2 (could be extended if necessary) 
     in output, gives a float vector as well but ordering the two jets, the more massive in 1st position 
   */ 


 mass_order::mass_order(float arg_mass) {mass = arg_mass;}
  ROOT::VecOps::RVec<TLorentzVector> mass_order::operator() (ROOT::VecOps::RVec<float> m, ROOT::VecOps::RVec<float> px,ROOT::VecOps::RVec<float> py, ROOT::VecOps::RVec<float>  pz, ROOT::VecOps::RVec<float> e ) {
  ROOT::VecOps::RVec<TLorentzVector> ordered;
  TLorentzVector tlv0;
  TLorentzVector tlv1; 
  tlv0.SetPxPyPzE(px[0],py[0],pz[0],e[0]);
  tlv1.SetPxPyPzE(px[1],py[1],pz[1],e[1]);
   if ( abs( mass - m[0] ) < abs( mass - m[1]) ) {
     ordered.push_back(tlv0);
     ordered.push_back(tlv1);
   }
   else {
     ordered.push_back(tlv1);
     ordered.push_back(tlv0);
   }

   return ordered;
  }


  

   
      

ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> findZleptons(const ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>& legs) {
  //ROOT::VecOps::RVec<bool> findZleptons(const ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>& legs) {

  int Zdau1(-1), Zdau2(-1);
  float Zmass(1e9);
  int n = legs.size();
  //ROOT::VecOps::RVec<bool> result(n);
  //std::fill(result.begin(), result.end(), false);
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;

  if (n>1) {
    ROOT::VecOps::RVec<bool> v(n);
    std::fill(v.end() - 2, v.end(), true);
    do {
      edm4hep::ReconstructedParticleData reso;
      TLorentzVector reso_lv;
      float m1(-999.), m2(-999.);
      int i1(-1), i2(-1);
      for (int i = 0; i < n; ++i) {
        if (v[i]) {
          reso.charge += legs[i].charge;
          TLorentzVector leg_lv;
          leg_lv.SetXYZM(legs[i].momentum.x, legs[i].momentum.y, legs[i].momentum.z, legs[i].mass);
          reso_lv += leg_lv;
	  if (m1<0) {
	    m1 = legs[i].mass;
	    i1 = i;
	  }
	  else {
	    m2 = legs[i].mass;
	    i2 = i;
	  }
        }
      }
      // CONSIDER ONLY OPPOSITE CHARGE SAME FLAVOUR COMBINATIONS
      // debug
      //std::cout << i1 << " " << i2 << std:: endl;
      //std::cout << reso.charge << std:: endl;
      //std::cout << m1-m2 << std:: endl;
      if (reso.charge==0 && std::abs(m1-m2)<1e-5) {
	reso.momentum.x = reso_lv.Px();
	reso.momentum.y = reso_lv.Py();
	reso.momentum.z = reso_lv.Pz();
        reso.mass = reso_lv.M();
	// debug
	//std::cout << reso.mass << std::endl;
	if (abs(reso.mass - 91.2)<abs(Zmass - 91.2)) {
	  Zmass = reso.mass;
	  Zdau1 = i1;
	  Zdau2 = i2;
	}
      }
    } while (std::next_permutation(v.begin(), v.end()));
  }
  if (Zdau1>-1 and Zdau2>-1) {
    // debug
    // std::cout << "Selected pair: " << Zdau1 << " " << Zdau2 << ", mass: " << Zmass << std::endl;
    //result[Zdau1] = true;
    //result[Zdau2] = true;
    result.push_back(legs[Zdau1]);
    result.push_back(legs[Zdau2]);
  }
  return result;
}





sel_pt::sel_pt(float arg_min_pt) : m_min_pt(arg_min_pt) {};
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  sel_pt::operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  result.reserve(in.size());
  for (size_t i = 0; i < in.size(); ++i) {
    auto & p = in[i];
    if (std::sqrt(std::pow(p.momentum.x,2) + std::pow(p.momentum.y,2)) > m_min_pt) {
      result.emplace_back(p);
    }
  }
  return result;
}


//____________________________________________________________


sel_mass::sel_mass(float arg_min_mass, float arg_max_mass) : m_min_mass(arg_min_mass), m_max_mass(arg_max_mass)  {};
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  sel_mass::operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  result.reserve(in.size());
  for (size_t i = 0; i < in.size(); ++i) {
    auto & p = in[i];
    if (p.mass > m_min_mass && p.mass < m_max_mass) {
      result.emplace_back(p);
    }
  }
  return result;
}

sel_recoil_mass::sel_recoil_mass(float arg_min_recoil_mass, float arg_max_recoil_mass) : m_min_recoil_mass(arg_min_recoil_mass), m_max_recoil_mass(arg_max_recoil_mass)  {};
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  sel_recoil_mass::operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  result.reserve(in.size());
  for (size_t i = 0; i < in.size(); ++i) {
    auto & p = in[i];
    TLorentzVector tlv;
    tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    float recoil = std::sqrt(std::pow(240 - tlv.E(), 2)-std::pow(tlv.P(), 2));    
    if (recoil > m_min_recoil_mass && recoil < m_max_recoil_mass) {
      result.emplace_back(p);
    }
  }
  return result;
}

ROOT::VecOps::RVec<float> get_recoil_mass(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    TLorentzVector tlv;
    tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    float recoil = std::sqrt(std::pow(240 - tlv.E(), 2)-std::pow(tlv.P(), 2));
    result.push_back(recoil);
  }
  return result;
}

ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> sel_recoilMassCloserToH(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> x, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> y) {
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  result.reserve(x.size());
  for (size_t i = 0; i < x.size(); i++) {
    auto & p = x[i];
    auto & q = y[i];
    TLorentzVector tlv_p;
    TLorentzVector tlv_q;
    tlv_p.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    tlv_q.SetXYZM(q.momentum.x, q.momentum.y, q.momentum.z, q.mass);
    float recoil_p = std::sqrt(std::pow(240 - tlv_p.E(), 2) - std::pow(tlv_p.P(), 2));
    float recoil_q = std::sqrt(std::pow(240 - tlv_q.E(), 2) - std::pow(tlv_q.P(), 2));
    if (abs(125 - recoil_p) < abs(125 - recoil_q)) result.emplace_back(p);
    else result.emplace_back(q);
  }
  return result;
}

edm4hep::ReconstructedParticleData sel_recoilMassCloserToH(edm4hep::ReconstructedParticleData p, edm4hep::ReconstructedParticleData q) {
  edm4hep::ReconstructedParticleData result;
  TLorentzVector tlv_p;
  TLorentzVector tlv_q;
  tlv_p.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
  tlv_q.SetXYZM(q.momentum.x, q.momentum.y, q.momentum.z, q.mass);
  float recoil_p = std::sqrt(std::pow(240 - tlv_p.E(), 2) - std::pow(tlv_p.P(), 2));
  float recoil_q = std::sqrt(std::pow(240 - tlv_q.E(), 2) - std::pow(tlv_q.P(), 2));
  if (abs(125 - recoil_p) < abs(125 - recoil_q)) result = p;
  else result = q;  
  return result;
}

edm4hep::ReconstructedParticleData sel_recoilMassFurtherFromH(edm4hep::ReconstructedParticleData p, edm4hep::ReconstructedParticleData q) {
  edm4hep::ReconstructedParticleData result;
  TLorentzVector tlv_p;
  TLorentzVector tlv_q;
  tlv_p.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
  tlv_q.SetXYZM(q.momentum.x, q.momentum.y, q.momentum.z, q.mass);
  float recoil_p = std::sqrt(std::pow(240 - tlv_p.E(), 2) - std::pow(tlv_p.P(), 2));
  float recoil_q = std::sqrt(std::pow(240 - tlv_q.E(), 2) - std::pow(tlv_q.P(), 2));
  if (abs(125 - recoil_p) < abs(125 - recoil_q)) result = q;
  else result = p;
  return result;
}

TLorentzVector set_tlvXYZM(const ROOT::VecOps::RVec<float> &px, const ROOT::VecOps::RVec<float> &py, const ROOT::VecOps::RVec<float> &pz, float m) {
  TLorentzVector result;
  result.SetXYZM(px[0], py[0], pz[0], m);
  return result;
}


//___________________________________________________________


sel_eta::sel_eta(float arg_min_eta) : m_min_eta(arg_min_eta) {};
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  sel_eta::operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  result.reserve(in.size());
  for (size_t i = 0; i < in.size(); ++i) {
    auto & p = in[i];
    TLorentzVector tv1;
    tv1.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    if (abs(tv1.Eta()) < abs(m_min_eta)){
      result.emplace_back(p);
    }
  }
  return result;
}





sel_p::sel_p(float arg_min_p, float arg_max_p) : m_min_p(arg_min_p), m_max_p(arg_max_p)  {};
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  sel_p::operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  result.reserve(in.size());
  for (size_t i = 0; i < in.size(); ++i) {
    auto & p = in[i];
    float momentum = std::sqrt(   std::pow(p.momentum.x,2)
                                + std::pow(p.momentum.y,2)
                                + std::pow(p.momentum.z,2) );
    if ( momentum > m_min_p && momentum < m_max_p ) {
      result.emplace_back(p);
    }
  }
  return result;
}

sel_charge::sel_charge(int arg_charge, bool arg_abs){m_charge = arg_charge; m_abs = arg_abs;};

ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  sel_charge::operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  result.reserve(in.size());
  for (size_t i = 0; i < in.size(); ++i) {
    auto & p = in[i];
    if ((m_abs && abs(in[i].charge)==m_charge) || (m_charge==in[i].charge) ) {
      result.emplace_back(p);
    }
  }
  return result;
}

resonanceBuilder::resonanceBuilder(float arg_resonance_mass) {m_resonance_mass = arg_resonance_mass;}
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> resonanceBuilder::operator()(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> legs) {
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  int n = legs.size();
  if (n >1) {
    ROOT::VecOps::RVec<bool> v(n);
    std::fill(v.end() - 2, v.end(), true);
    do {
      edm4hep::ReconstructedParticleData reso;
      TLorentzVector reso_lv;
      for (int i = 0; i < n; ++i) {
          if (v[i]) {
            reso.charge += legs[i].charge;
            TLorentzVector leg_lv;
            leg_lv.SetXYZM(legs[i].momentum.x, legs[i].momentum.y, legs[i].momentum.z, legs[i].mass);
            reso_lv += leg_lv;
          }
      }
      reso.momentum.x = reso_lv.Px();
      reso.momentum.y = reso_lv.Py();
      reso.momentum.z = reso_lv.Pz();
      reso.mass = reso_lv.M();
      result.emplace_back(reso);
    } while (std::next_permutation(v.begin(), v.end()));
  }
  if (result.size() > 1) {
    auto resonancesort = [&] (edm4hep::ReconstructedParticleData i ,edm4hep::ReconstructedParticleData j) { return (abs( m_resonance_mass -i.mass)<abs(m_resonance_mass-j.mass)); };
    std::sort(result.begin(), result.end(), resonancesort);
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>::const_iterator first = result.begin();
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>::const_iterator last = result.begin() + 1;
    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> onlyBestReso(first, last);
    return onlyBestReso;
  } else {
    return result;
  }
}


	  






recoilBuilder::recoilBuilder(float arg_sqrts) : m_sqrts(arg_sqrts) {};
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>  recoilBuilder::operator() (ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  auto recoil_p4 = TLorentzVector(0, 0, 0, m_sqrts);
  for (auto & v1: in) {
    TLorentzVector tv1;
    tv1.SetXYZM(v1.momentum.x, v1.momentum.y, v1.momentum.z, v1.mass);
    recoil_p4 -= tv1;
  }
  auto recoil_fcc = edm4hep::ReconstructedParticleData();
  recoil_fcc.momentum.x = recoil_p4.Px();
  recoil_fcc.momentum.y = recoil_p4.Py();
  recoil_fcc.momentum.z = recoil_p4.Pz();
  recoil_fcc.mass = recoil_p4.M();
  result.push_back(recoil_fcc);
  return result;
};


multijetResonanceBuilder::multijetResonanceBuilder(float arg_resonance_mass, int nlegs, int strategy) {m_resonance_mass = arg_resonance_mass; m_nlegs = nlegs; m_strategy=strategy; }
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> multijetResonanceBuilder::operator()(const ROOT::VecOps::RVec<fastjet::PseudoJet> & legs) {
      ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
      int n = legs.size();
      if (m_nlegs>n) m_nlegs = n;
      if (n >= m_nlegs && n>1) {// do not build resonances if there are <2 legs or if size of legs vector is < of requested nlegs
        ROOT::VecOps::RVec<bool> v(n);
        //std::fill(v.end() - m_nlegs, v.end(), true);
        std::fill(v.begin(), v.end(), false);
        std::fill(v.begin(), v.begin()+m_nlegs, true);
        int nperm=0;
        do {
          // check if we only want to build resonance from first n legs
          if (nperm>0 && m_strategy==2) continue;
        
          edm4hep::ReconstructedParticleData reso;
          // without the following line the charge will assume random values
          reso.charge = 0;
          TLorentzVector reso_lv; 
          for (int i = 0; i < n; ++i) {
              if (v[i]) {
                TLorentzVector leg_lv;
                leg_lv.SetXYZM(legs[i].px(), legs[i].py(), legs[i].pz(), legs[i].m());
                reso_lv += leg_lv;
              }
          }
          reso.momentum.x = reso_lv.Px();
          reso.momentum.y = reso_lv.Py();
          reso.momentum.z = reso_lv.Pz();
          reso.energy = reso_lv.E();
          reso.mass = reso_lv.M();
          result.emplace_back(reso);
          nperm++;
        } while (std::prev_permutation(v.begin(), v.end()));
      }
      if (result.size() > 1 && m_strategy==1) {
        auto resonancesort = [&] (edm4hep::ReconstructedParticleData i ,edm4hep::ReconstructedParticleData j) { return (abs( m_resonance_mass -i.mass)<abs(m_resonance_mass-j.mass)); };
        std::sort(result.begin(), result.end(), resonancesort);
        ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>::const_iterator first = result.begin();
        ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>::const_iterator last = result.begin() + 1;
        ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> onlyBestReso(first, last);
        return onlyBestReso;
      } else {
        return result;
      }
    }


sel_axis::sel_axis(bool arg_pos): m_pos(arg_pos) {};
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> sel_axis::operator()(ROOT::VecOps::RVec<float> angle, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in){
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  for (size_t i = 0; i < angle.size(); ++i) {
    if (m_pos==1 && angle.at(i)>0.) result.push_back(in.at(i));
    if (m_pos==0 && angle.at(i)<0.) result.push_back(in.at(i));;
  }
  return result;
}


sel_tag::sel_tag(bool arg_pass): m_pass(arg_pass) {};
ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> sel_tag::operator()(ROOT::VecOps::RVec<bool> tags, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in){
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  for (size_t i = 0; i < in.size(); ++i) {
    if (m_pass) {
      if (tags.at(i)) result.push_back(in.at(i));
    }
    else {
      if (!tags.at(i)) result.push_back(in.at(i));
    }
  }
  return result;
}



// Angular separation between the particles of a collection:
//   arg_delta = 0 / 1 / 2 :   return delta_max, delta_min, delta_average

angular_separationBuilder::angular_separationBuilder( int  arg_delta) : m_delta(arg_delta) {};
float angular_separationBuilder::operator() ( ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {

 float result = -9999;

 float dmax = -999;
 float dmin = 999;
 float sum = 0;
 float npairs = 0;
 for (int i=0; i < in.size(); i++) {
  if ( in.at(i).energy < 0) continue;    // "dummy" particle - cf selRP_matched_to_list
  TVector3 p1( in.at(i).momentum.x, in.at(i).momentum.y, in.at(i).momentum.z );
  for (int j=i+1; j < in.size(); j++) {
    if ( in.at(j).energy < 0) continue;   // "dummy" particle
    TVector3 p2( in.at(j).momentum.x, in.at(j).momentum.y, in.at(j).momentum.z );
    float delta_ij = fabs( p1.Angle( p2 ) );
    if ( delta_ij > dmax) dmax = delta_ij;
    if ( delta_ij < dmin) dmin = delta_ij;
    sum = sum + delta_ij;
    npairs ++;
  }
 }
 float delta_max = dmax;
 float delta_min = dmin;
 float delta_ave = sum / npairs;

 if (m_delta == 0 ) result = delta_max;
 if (m_delta == 1 ) result = delta_min;
 if (m_delta == 2 ) result = delta_ave;

 return result;
}


ROOT::VecOps::RVec<float> get_pt(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in){
 ROOT::VecOps::RVec<float> result;
 for (size_t i = 0; i < in.size(); ++i) {
   result.push_back(sqrt(in[i].momentum.x * in[i].momentum.x + in[i].momentum.y * in[i].momentum.y));
 }
 return result;
}

ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> merge(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> x, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> y) {
  //to be keept as ROOT::VecOps::RVec
  std::vector<edm4hep::ReconstructedParticleData> result;
  result.reserve(x.size() + y.size());
  result.insert( result.end(), x.begin(), x.end() );
  result.insert( result.end(), y.begin(), y.end() );
  return ROOT::VecOps::RVec(result);
}


ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> remove(
  		ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> x,
  		ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> y) {
  //to be kept as ROOT::VecOps::RVec
  std::vector<edm4hep::ReconstructedParticleData> result;
  result.reserve( x.size() );
  result.insert( result.end(), x.begin(), x.end() );
  float epsilon = 1e-8;
  for (size_t i = 0; i < y.size(); ++i) {
    float mass1 = y.at(i).mass;
    float px1 = y.at(i).momentum.x;
    float py1 = y.at(i).momentum.y;
    float pz1 = y.at(i).momentum.z;
    for(std::vector<edm4hep::ReconstructedParticleData>::iterator
          it = std::begin(result); it != std::end(result); ++it) {
      float mass2 = it->mass;
      float px2 = it->momentum.x;
      float py2 = it->momentum.y;
      float pz2 = it->momentum.z;
      if ( abs(mass1-mass2) < epsilon &&
	   abs(px1-px2) < epsilon &&
	   abs(py1-py2) < epsilon &&
	   abs(pz1-pz2) < epsilon ) {
        result.erase(it);
        break;
      }
    }
  }
  return ROOT::VecOps::RVec(result);
}




ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> get(ROOT::VecOps::RVec<int> index, ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in){
  ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;
  for (size_t i = 0; i < index.size(); ++i) {
    if (index[i]>-1)
      result.push_back(in.at(index[i]));
    //else
    //  std::cout << "electron index negative " << index[i]<<std::endl;
  }
  return result;
}

TLorentzVector get_P4vis(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
    TLorentzVector P4sum;
    for (auto & p: in) {
      TLorentzVector tlv;
      tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
      P4sum += tlv;
    }
    return P4sum;
  }


  TLorentzVector get_tlv_easy(float e, float px, float py, float pz){
    TLorentzVector tlv; 
    tlv.SetPxPyPzE(px, py , pz , e); 
    return tlv;
  }



ROOT::VecOps::RVec<float> get_mass(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    result.push_back(p.mass);
  }
  return result;
}

ROOT::VecOps::RVec<float> get_eta(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    TLorentzVector tlv;
    tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    result.push_back(tlv.Eta());
  }
  return result;
}

ROOT::VecOps::RVec<float> get_phi(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    TLorentzVector tlv;
    tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    result.push_back(tlv.Phi());
  }
  return result;
}

ROOT::VecOps::RVec<float> get_e(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    result.push_back(p.energy);
  }
  return result;
}

ROOT::VecOps::RVec<float> get_p(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    TLorentzVector tlv;
    tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    result.push_back(tlv.P());
  }
  return result;
}

ROOT::VecOps::RVec<float> get_px(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    result.push_back(p.momentum.x);
  }
  return result;
}


ROOT::VecOps::RVec<float> get_py(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    result.push_back(p.momentum.y);
  }
  return result;
}

ROOT::VecOps::RVec<float> get_pz(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    result.push_back(p.momentum.z);
  }
  return result;
}

ROOT::VecOps::RVec<float> get_charge(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    result.push_back(p.charge);
  }
  return result;
}

ROOT::VecOps::RVec<float> get_y(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    TLorentzVector tlv;
    tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    result.push_back(tlv.Rapidity());
  }
  return result;
}

ROOT::VecOps::RVec<float> get_theta(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    TLorentzVector tlv;
    tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    result.push_back(tlv.Theta());
  }
  return result;
}

ROOT::VecOps::RVec<float> get_costheta(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: in) {
    TLorentzVector tlv;
    tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    result.push_back(cos(tlv.Theta()));
  }
  return result;
}


ROOT::VecOps::RVec<TLorentzVector> get_tlv(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in) {
  ROOT::VecOps::RVec<TLorentzVector> result;
  for (auto & p: in) {
    TLorentzVector tlv;
    tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    result.push_back(tlv);
  }
  return result;
}

TLorentzVector get_tlv(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in, int index) {
  TLorentzVector result;
  auto & p = in[index];
  result.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
  return result;
}

TLorentzVector get_tlv(edm4hep::ReconstructedParticleData in) {
  TLorentzVector result;
  result.SetXYZM(in.momentum.x, in.momentum.y, in.momentum.z, in.mass);
  return result;
}

ROOT::VecOps::RVec<int>
get_type(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> in){
  ROOT::VecOps::RVec<int> result;
  for (auto & p: in) {
    result.push_back(p.type);
  }
  return result;
}


int get_n(ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> x) {
  int result =  x.size();
  return result;
}


ROOT::VecOps::RVec<bool> getJet_btag(ROOT::VecOps::RVec<int> index, ROOT::VecOps::RVec<edm4hep::ParticleIDData> pid, ROOT::VecOps::RVec<float> values){
  ROOT::VecOps::RVec<bool> result;
  //std::cout << "========================new event=======================" <<std::endl;
  for (size_t i = 0; i < index.size(); ++i) {
    result.push_back(values.at(pid.at(index.at(i)).parameters_begin));

    //std::cout << pid.at(index.at(i)).parameters_begin << "  ==  " << pid.at(index.at(i)).parameters_end << std::endl;
    //for (unsigned j = pid.at(index.at(i)).parameters_begin; j != pid.at(index.at(i)).parameters_end; ++j) {
    //  std::cout << " values : " << values.at(j) << std::endl;
    //}
  }
  return result;
}

int getJet_ntags(ROOT::VecOps::RVec<bool> in) {
  int result =  0;
  for (size_t i = 0; i < in.size(); ++i)
    if (in.at(i))result+=1;
  return result;
}



}//end NS ReconstructedParticle

}//end NS FCCAnalyses
