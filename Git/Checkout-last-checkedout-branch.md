# Checkout last checked-out branch

you know that `cd -` change your current directory to the last path you were in, `git checkout` uses the same convention, hence `git checkout -` will check out the last branch you checked.

		$ git branch

		  feature_infra/ansible_optimisation
			feature_infra/dev_selfcare
			feature_infra/rebase_user_role
			feature_infra/web-rec-public-register
		* feature_tools/docker_in_docker
			feature_tools/update_fab_vagrant
			feature_web/fix_account_flask_api_version
			master

		$ git checkout master
		$ git branch

			feature_infra/ansible_optimisation
			feature_infra/dev_selfcare
			feature_infra/rebase_user_role
			feature_infra/web-rec-public-register
			feature_tools/docker_in_docker
			feature_tools/update_fab_vagrant
			feature_web/fix_account_flask_api_version
		* master

		$ git checkout -

		  feature_infra/ansible_optimisation
			feature_infra/dev_selfcare
			feature_infra/rebase_user_role
			feature_infra/web-rec-public-register
		* feature_tools/docker_in_docker
			feature_tools/update_fab_vagrant
			feature_web/fix_account_flask_api_version
			master
