
#include "effect_defaults.h"


int new_data_ready_flg;

// DEFINES
#define DELAY_BUFFER_LENGTH  24000



typedef struct delay_parameters_st{
	float 		time_f32; 					// in ms
	uint32_t 	time_in_buffer_u32; 		// in buffer location 1 = 1/48 ms
	uint32_t 	modulation_in_buffer_u32;	// sets the modulation of the delay
	uint32_t	modulation_counter_u32;
	int32_t		modulation_amplitude_i32;
	uint32_t 	modulation_base_u32;
	float 		mix_f32;  					// delay and input
	uint8_t 	repeats_u8;					// number of repeats
	float   	feedback_gain_f32;			// how repeats weaken over time
}delay_parameters_tst;

typedef struct delay_effects_st{
	int32_t 				input_i32;
	int32_t 				output_i32;
	int32_t*				buffer_ai32;

	// pointers
	uint32_t 				current_counter_u32;
	uint32_t 				delayed_counter_u32;
	uint8_t					modulation_on_u8;
	delay_parameters_tst 	parameters_st;

	// functions
	int32_t (*callback) (struct delay_effects_st* self,int32_t input_signal_i32);
}delay_effects_tst;


// void process_delay_fx();


void init_periferials(){
};
void load_presets_from_flash(){
};


// Process one effect

// Process 3 effects in Loop




// pre
void process_effect_chain(effect_chain_tst* fx_chain_ptr,effect_chain_tst* fx_chain_requested_ptr, float* input_ptr,float* output_ptr){
    if ( fx_chain_ptr->preset_num_st.major != fx_chain_requested_ptr->preset_num_st.major){
        // Free memory from this
        free_memory(fx_chain_ptr);
        // set new presets
        fx_chain_ptr->preset_num_st = fx_chain_ptr.
        // Alloc new presets memory
        alloc_memory(fx_chain_ptr)
    }
};

uint32_t input_u32[4];
uint32_t output_u32[4];

int main(){

    
    /*SETUP*/
    init_periferials();
    load_presets_from_flash();

    effect_chain_tst* fx_chain;
    effect_chain_tst* fx_chain_requested;

    /*LOOP*/
    while(1){
        if(new_data_ready_flg){
            process_effect_chain(fx_chain,fx_chain_requested,input_u32,output_u32);
            
        }
    }
}
