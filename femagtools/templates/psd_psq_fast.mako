--
-- Psid-Psiq- Identification
--
	 
m.move_action     =    0.0 -- rotate 
m.arm_length      =    ${model.get('lfe')*1e3}
m.num_pol_pair    =    m.num_poles/2
m.speed           =    ${model.get('speed')*60}
m.skew_angle      =    ${model.get('skew_angle',0)}
m.nu_skew_steps   =    ${model.get('num_skew_steps',0)}
m.magn_temp       =    ${model.get('magn_temp')}
m.fc_mult_move_type =  1.0 --  Type of move path in air gap
m.phi_start       =    0.0 --  
m.range_phi       =    720./m.num_poles
m.nu_move_steps   =    ${model.get('num_move_steps')}
m.num_par_wdgs    =    ${model.get('num_par_wdgs',1)}

m.maxid           =    ${model['maxid']}/m.num_par_wdgs
m.minid           =    ${model['minid']}/m.num_par_wdgs
m.maxiq           =    ${model['maxiq']}/m.num_par_wdgs
m.miniq           =    ${model['miniq']}/m.num_par_wdgs
m.delta_id        =    ${model['delta_id']}/m.num_par_wdgs
m.delta_iq        =    ${model['delta_iq']}/m.num_par_wdgs

m.pm_eff_aktiv    =    0.0

m.pocfilename    = model..'_'..m.num_poles..'p.poc'

run_models("psd_psq_fast")
