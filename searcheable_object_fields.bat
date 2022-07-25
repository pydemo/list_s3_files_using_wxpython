set AWS_PROFILE=au-olek
set ZZZ_RUNTIME_ENV__=DEV
set ZZZ_STACK_NAME__=Pipline.AU
python cli.py  -nop 2 -r DEV -p aws\list_pipelines -pa filter limit -ui searcheable_object_fields
