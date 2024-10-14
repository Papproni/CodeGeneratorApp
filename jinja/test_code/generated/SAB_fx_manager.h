/*THIS FILE IS GENERATED! DO NOT MODIFY!
Generated on: 2024.10.13. */

#ifndef SAB_FX_MANAGER_H
#define SAB_FX_MANAGER_H


#include "stdint.h"

// Generated effect libs
#include "SAB_delay.h"
#include "SAB_overdrive.h"
#include "SAB_distortion.h"
#include "SAB_octave.h"
#include "SAB_flanger.h"
#include "SAB_chorus.h"
#include "SAB_boost.h"
#include "SAB_pitchshift.h"
#include "SAB_fuzz.h"


// Manager structure: fx_manager
typedef struct {
} SAB_fx_manager_tst;


// Process Function for SAB_fx_manager_tst
int SAB_fx_manager_init( SAB_fx_manager_tst* self, float input_f32, float output_f32);

// Process Function for SAB_fx_manager_tst
int SAB_fx_manager_process( SAB_fx_manager_tst* self, float input_f32, float output_f32);

// Enum representing different effect types
typedef enum {
    DELAY,
    OVERDRIVE,
    DISTORTION,
    OCTAVE,
    FLANGER,
    CHORUS,
    BOOST,
    PITCHSHIFT,
    FUZZ,
} EffectType;

// Struct for a guitar effect with function pointers
typedef struct {
    EffectType type;
    Effectstate_ten state;
    void (*init)(void*);           // Function pointer to initialize the effect
    void (*copy_from_flash)(void*); // Function pointer to copy data from flash
    void (*process)(void*);         // Function pointer to process the effect
} GuitarEffect;

typedef enum {
    FX_ACTIVE,
    FX_BYPASSED
} Effectstate_ten;

void init_effect_chain(GuitarEffect** chain, EffectType* fx_chain, int chain_length) {
    for (int i = 0; i < chain_length; ++i) {
        switch (fx_chain[i]) {
        case DELAY:
            chain[i] = (GuitarEffect*)malloc(sizeof(delayeffect));
            chain[i]->type = DELAY;
            chain[i]->init = init_delay;
            chain[i]->copy_from_flash = copy_delay_from_flash;
            chain[i]->process = process_delay;
            break;
        case OVERDRIVE:
            chain[i] = (GuitarEffect*)malloc(sizeof(overdriveeffect));
            chain[i]->type = OVERDRIVE;
            chain[i]->init = init_overdrive;
            chain[i]->copy_from_flash = copy_overdrive_from_flash;
            chain[i]->process = process_overdrive;
            break;
        case DISTORTION:
            chain[i] = (GuitarEffect*)malloc(sizeof(distortioneffect));
            chain[i]->type = DISTORTION;
            chain[i]->init = init_distortion;
            chain[i]->copy_from_flash = copy_distortion_from_flash;
            chain[i]->process = process_distortion;
            break;
        case OCTAVE:
            chain[i] = (GuitarEffect*)malloc(sizeof(octaveeffect));
            chain[i]->type = OCTAVE;
            chain[i]->init = init_octave;
            chain[i]->copy_from_flash = copy_octave_from_flash;
            chain[i]->process = process_octave;
            break;
        case FLANGER:
            chain[i] = (GuitarEffect*)malloc(sizeof(flangereffect));
            chain[i]->type = FLANGER;
            chain[i]->init = init_flanger;
            chain[i]->copy_from_flash = copy_flanger_from_flash;
            chain[i]->process = process_flanger;
            break;
        case CHORUS:
            chain[i] = (GuitarEffect*)malloc(sizeof(choruseffect));
            chain[i]->type = CHORUS;
            chain[i]->init = init_chorus;
            chain[i]->copy_from_flash = copy_chorus_from_flash;
            chain[i]->process = process_chorus;
            break;
        case BOOST:
            chain[i] = (GuitarEffect*)malloc(sizeof(boosteffect));
            chain[i]->type = BOOST;
            chain[i]->init = init_boost;
            chain[i]->copy_from_flash = copy_boost_from_flash;
            chain[i]->process = process_boost;
            break;
        case PITCHSHIFT:
            chain[i] = (GuitarEffect*)malloc(sizeof(pitchshifteffect));
            chain[i]->type = PITCHSHIFT;
            chain[i]->init = init_pitchshift;
            chain[i]->copy_from_flash = copy_pitchshift_from_flash;
            chain[i]->process = process_pitchshift;
            break;
        case FUZZ:
            chain[i] = (GuitarEffect*)malloc(sizeof(fuzzeffect));
            chain[i]->type = FUZZ;
            chain[i]->init = init_fuzz;
            chain[i]->copy_from_flash = copy_fuzz_from_flash;
            chain[i]->process = process_fuzz;
            break;
        default:
            printf("Unknown effect type!\n");
            break;
        }
        // Initialize the effect
        chain[i]->init(chain[i]);
        // Copy data from flash (simulated)
        chain[i]->copy_from_flash(chain[i]);
    }
}

#endif