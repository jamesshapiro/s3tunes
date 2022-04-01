#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s3tunes.s3tunes_stack import S3TunesStack


app = cdk.App()
S3TunesStack(app, "S3TunesStack",
    env={'region': 'us-east-1'}
)

app.synth()
