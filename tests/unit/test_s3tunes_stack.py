import aws_cdk as core
import aws_cdk.assertions as assertions

from s3tunes.s3tunes_stack import S3TunesStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3tunes/s3tunes_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3TunesStack(app, "s3tunes")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
