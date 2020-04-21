import json
import sys
from pathlib import Path

from datetime import datetime as dt

from thoth.common import Workflow
from thoth.common import WorkflowManager

from thoth.common.logging import init_logging
from thoth.common.openshift import OpenShift

init_logging({'thoth.common.workflows': 'INFO'})

workflow_id = f"-{int(dt.now().timestamp())}"
use_argo = False
use_openshift = True

if use_argo:
    workflow_manager = WorkflowManager(openshift=OpenShift(kubernetes_verify_tls=False))
    template_parameters = {
        "WORKFLOW_ID": workflow_id,
        "GITHUB_EVENT_TYPE": "thoth_thamos_advise",
        "GITHUB_CHECK_RUN_ID": 452891565,
        "GITHUB_INSTALLATION_ID": 6181026,
        "ORIGIN": "https://github.com/thoth-station/package-update-job",
        "GITHUB_HEAD_REPO_URL": "https://github.com/thoth-station/package-update-job",
        "GITHUB_BASE_REPO_URL": "https://api.github.com/repos/thoth-station/package-update-job",
        "REVISION": "8c7dfad215860d508b7ea63613d5b86c0198c592",
        "THOTH_HOST":  "stage.thoth-station.ninja"
    }

    workflow_parameters = {}

    workflow_id = workflow_manager.submit_thamos_workflow(
        template_parameters=template_parameters,
        workflow_parameters=workflow_parameters
    )

    print(workflow_id)

if use_openshift:
    openshift = OpenShift()
    workflow_id = openshift.schedule_thamos_workflow(
        github_event_type="thoth_thamos_advise",
        github_check_run_id=592585217,
        github_installation_id=8041620,
        github_base_repo_url="https://api.github.com/repos/llunved/home-assistant-core",
        github_head_repo_url="https://github.com/llunved/home-assistant-core",
        origin="https://github.com/llunved/home-assistant-core",
        revision="b25b69179c36703817c86ff7018fb21e37da2754",
        host="stage.thoth-station.ninja",
    )
    print(workflow_id)
