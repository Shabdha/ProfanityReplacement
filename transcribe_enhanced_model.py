#!/usr/bin/env python

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample that demonstrates enhanced models
and recognition metadata.

Example usage:
    python transcribe_enhanced_model.py resources/commercial_mono.wav
"""
# import argparse

import io
from google.cloud import speech
from scipy.io import wavfile
import scipy.signal as sps


def transcribe_file_with_enhanced_model(path, lang):
    """Transcribe the given audio file using an enhanced model."""
    # [START speech_transcribe_enhanced_model]
    # new_rate = 8000
    sampling_rate, data = wavfile.read(path)
    # number_of_samples = round(len(data) * float(new_rate) / sampling_rate)
    # data = sps.resample(data, number_of_samples)

    client = speech.SpeechClient()
    with io.open(path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.types.RecognitionAudio(content=content)
    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sampling_rate,
        language_code=lang,
        # Enhanced models are only available to projects that
        # opt in for audio data collection.
        use_enhanced=True,
        # A model must be specified to use enhanced model.
        model='default')

    response = client.recognize(config, audio)
    f=open("transcript.txt","w+",encoding="utf-8")
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print('-' * 20)
        print('First alternative of result {}'.format(i))
        print('Transcript: {}'.format(alternative.transcript))
        f.write('{}'.format(alternative.transcript) )
    # [END speech_transcribe_enhanced_model]
    f.close()


#transcribe_file_with_enhanced_model('blood_audio.wav')