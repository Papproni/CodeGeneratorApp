/*THIS FILE IS GENERATED! DO NOT MODIFY!
Generated on: 2024.11.28. */

#ifndef SAB_CHORUS_H
#define SAB_CHORUS_H

#include "SAB_chorus.h"

void SAB_chorus_delete( SAB_chorus_tst* self){
    // TODO
}


// Process Function for SAB_chorus_tst
void SAB_chorus_init( SAB_chorus_tst* self){
    strcpy(self->intercom_fx_data.name, "chorus");
	self->intercom_fx_data.color[0] = 255; 	// R
	self->intercom_fx_data.color[1] = 0;	// G
	self->intercom_fx_data.color[2] = 0;	// B
	self->intercom_fx_data.fx_state_en = FX_STATE_OFF;

	// PARAMS:
    
    add_parameter(&self->intercom_parameters_aun[0],"NONE",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[1],"NONE",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[2],"NONE",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[3],"GAIN",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[4],"NONE",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[5],"NONE",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[6],"NONE",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[7],"NONE",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[8],"NONE",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[9],"NONE",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[10],"NONE",PARAM_TYPE_POT,69);
    add_parameter(&self->intercom_parameters_aun[11],"NONE",PARAM_TYPE_POT,69);
};

// Process Function for SAB_chorus_tst
float32_t SAB_chorus_process( SAB_chorus_tst* self, float input_f32){
    // TODO
};
