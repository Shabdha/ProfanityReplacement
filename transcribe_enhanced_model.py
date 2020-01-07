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
        enable_word_time_offsets=True,
        # A model must be specified to use enhanced model.
        model='default')

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    # The first result includes start and end time word offsets
    result = response.results[0]
    # First alternative is the most probable result
    alternative = result.alternatives[0]
    print(u"Transcript: {}".format(alternative.transcript))
    # Print the start and end time of each word
    f = open("transcript.txt", "w+", encoding="utf-8")
    for word in alternative.words:
        print(u"Word: {}".format(word.word))
        print(
            u"Start time: {} seconds {} milliseconds".format(
                word.start_time.seconds, word.start_time.nanos/1000000
            )
        )
        print(
            u"End time: {} seconds {} milliseconds".format(
                word.end_time.seconds, word.end_time.nanos/1000000
            )
        )
        f.write('{} / {} {} / {} {} - '.format(word.word,  word.start_time.seconds,word.start_time.nanos/1000000, word.end_time.seconds, word.end_time.nanos/1000000))
    # response = client.recognize(config, audio)
    #
    # for i, result in enumerate(response.results):
    #     alternative = result.alternatives[0]
    #     print('-' * 20)
    #     print('First alternative of result {}'.format(i))
    #     print('Transcript: {}'.format(alternative.transcript))
    #     f.write('{}'.format(alternative.transcript) )
    # # [END speech_transcribe_enhanced_model]
    f.close()


#transcribe_file_with_enhanced_model('sample03.wav','en-US')