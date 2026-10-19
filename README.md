# Back-End-Development-Pictures

Flask REST API for the IBM Back-End Development Capstone. Routes follow the
course's Pictures service exercises. Includes a Dockerfile and 11 automated tests.

## API endpoints

| HTTP | Path | Purpose |
| --- | --- | --- |
| GET | `/health` | `{"status":"OK"}` |
| GET | `/count` | Number of picture entries |
| GET | `/picture` | All picture entries |
| GET | `/picture/<id>` | One picture (404 if missing) |
| POST | `/picture` | Create a picture (201, or 302 if duplicate as required by course) |
| PUT | `/picture/<id>` | Update an existing picture |
| DELETE | `/picture/<id>` | Delete a picture (204) |

Example fields are `id`, `pic_url`, `event_country`, `event_state`,
`event_city`, `event_date`. The service starts with **10 pictures**.
This is an educational in-memory app; mutations are not persisted.

## Set up inside Skills Network Cloud IDE

Upload `Back-End-Development-Pictures.zip` to `/home/project`, then:

```bash
cd /home/project
unzip Back-End-Development-Pictures.zip
cd Back-End-Development-Pictures
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -v
```

Run locally inside the Cloud IDE:

```bash
flask --app app run --host 0.0.0.0 --port 5000
# in another terminal
curl http://localhost:5000/health
curl http://localhost:5000/count
```

## IBM Code Engine deployment (graded question 17)

The Skills Network Code Engine project should show READY TO USE. Open
Code Engine CLI, and from this project directory run:

```bash
ibmcloud ce project current
ibmcloud ce app create --name pictures --build-source . --build-strategy dockerfile --port 8080
ibmcloud ce app get --name pictures
```

Copy the **real** full success output of the `app create` command into Q17.
If the remote build/registry is unavailable due to temporary lab permissions,
use the displayed error to troubleshoot; do not fabricate success.

The command is based on [IBM Code Engine local-source deployment documentation](https://cloud.ibm.com/docs/codeengine?topic=codeengine-app-local-source-code).

## Evidence for capstone questions 2–5

Run in Cloud IDE. Screenshots should show the actual terminal outputs.
The commands below each save a text copy using `tee`:

```bash
mkdir -p evidence
pytest -v -k 'test_health or test_count' | tee evidence/exercise1-count-health-passing.txt
pytest -v -k 'test_data_contains_10_pictures or test_get_picture or test_pictures_json_is_not_empty' | tee evidence/exercise2-get-pictures-passing.txt
pytest -v -k 'test_post_picture' | tee evidence/exercise4-post-picture-passing.txt
pytest -v -k 'test_update_picture_by_id or test_delete_picture_by_id' | tee evidence/exercise6-delete-picture-passing.txt
```

The Coursera prompt requests exact outputs under the respective evidence names.
Capture your screen yourself if the item requires a screenshot; text outputs can
be copied directly to the appropriate text question.

## GitHub for capstone question 1

Create a **public** GitHub repository named precisely
`Back-End-Development-Pictures`. Upload these source files to its main branch.
Submit this file's actual public GitHub URL, in the form
`https://github.com/YOUR_USERNAME/Back-End-Development-Pictures/blob/main/README.md`.
Replace `YOUR_USERNAME` with your real GitHub username.

## Notes

- Do not include credentials or cloud secrets in GitHub.
- The source is an independently prepared educational implementation aligned with
  the described IBM lab interface, not a clone of the original starter repository.
