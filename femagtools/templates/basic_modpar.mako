  global_unit(mm)
  pickdist(0.001)
  cosys(polar)

<%include file="fe-contr.mako" />

ag  = ${model.get(['airgap'])*1e3}
% if model.move_action == 0:
% if model.external_rotor:
dy2 = ${model.get(['outer_diam'])*1e3}
da2 = ${model.get(['bore_diam'])*1e3}
dy1 = ${model.get(['inner_diam'])*1e3}
da1 = da2 - 2*ag 
% else:
dy1 = ${model.get(['outer_diam'])*1e3}
da1 = ${model.get(['bore_diam'])*1e3}
dy2 = ${model.get(['inner_diam'])*1e3}
da2 = da1 - 2*ag 
% endif
% endif

m.tot_num_slot    =   ${int(model.get(['stator','num_slots']))}
m.num_sl_gen      =   ${int(model.get(['stator','num_slots_gen']))}
m.num_poles       =   ${int(model.get(['poles']))}
m.num_slots       =   m.num_sl_gen 
m.npols_gen       =   m.num_poles * m.num_sl_gen / m.tot_num_slot
m.tot_num_sl      =   m.tot_num_slot
% if model.move_action == 0:
m.fc_radius       =   (da1+da2)/4
% endif
pre_models("basic_modpar")
