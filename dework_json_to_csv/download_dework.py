import requests
import json

url = "https://api.deworkxyz.com/graphql"

# get the list of workspaces in Comms DAO Dework Organisation

payload = json.dumps({
  "operationName": "GetOrganizationDetailsQuery",
  "variables": {
    "organizationId": "22a00c04-c013-4af6-bcbe-9a5356d3cd9c"
  },
  "query": "query GetOrganizationDetailsQuery($organizationId: UUID!) {\n  organization: getOrganization(id: $organizationId) {\n    ...OrganizationDetails\n    __typename\n  }\n}\n\nfragment OrganizationDetails on Organization {\n  ...Organization\n  tagline\n  description\n  options {\n    roadmap\n    roles\n    mintTaskNFTs\n    __typename\n  }\n  workspaceCount\n  workspaces {\n    ...Workspace\n    __typename\n  }\n  workspaceSections {\n    ...WorkspaceSection\n    __typename\n  }\n  tags {\n    ...OrganizationTag\n    __typename\n  }\n  details {\n    ...EntityDetail\n    __typename\n  }\n  workspaceTokenGates {\n    ...WorkspaceTokenGate\n    __typename\n  }\n  taskViews {\n    ...TaskView\n    __typename\n  }\n  fundingSessions {\n    ...FundingSession\n    __typename\n  }\n  node {\n    ...GraphNode\n    __typename\n  }\n  __typename\n}\n\nfragment Organization on Organization {\n  id\n  name\n  imageUrl\n  slug\n  tagline\n  description\n  permalink\n  nodeId\n  __typename\n}\n\nfragment Workspace on Workspace {\n  id\n  slug\n  name\n  icon\n  type\n  status\n  description\n  startAt\n  endAt\n  deletedAt\n  organizationId\n  permalink\n  sectionId\n  parentId\n  sortKey\n  roadmapSortKey\n  options {\n    showCommunitySuggestions\n    __typename\n  }\n  __typename\n}\n\nfragment WorkspaceSection on WorkspaceSection {\n  id\n  name\n  slug\n  layout\n  sortKey\n  organizationId\n  __typename\n}\n\nfragment OrganizationTag on OrganizationTag {\n  id\n  label\n  color\n  createdAt\n  __typename\n}\n\nfragment EntityDetail on EntityDetail {\n  id\n  type\n  value\n  __typename\n}\n\nfragment WorkspaceTokenGate on WorkspaceTokenGate {\n  id\n  role\n  workspaceId\n  token {\n    ...PaymentToken\n    network {\n      ...PaymentNetwork\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PaymentToken on PaymentToken {\n  id\n  exp\n  type\n  name\n  symbol\n  address\n  identifier\n  usdPrice\n  networkId\n  visibility\n  imageUrl\n  __typename\n}\n\nfragment PaymentNetwork on PaymentNetwork {\n  id\n  slug\n  name\n  type\n  config\n  sortKey\n  __typename\n}\n\nfragment TaskView on TaskView {\n  id\n  name\n  slug\n  type\n  icon\n  groupBy\n  permalink\n  workspaceId\n  workspaceSectionId\n  organizationId\n  userId\n  fields\n  sortKey\n  filters {\n    ...TaskViewFilter\n    __typename\n  }\n  sortBys {\n    ...TaskViewSortBy\n    __typename\n  }\n  __typename\n}\n\nfragment TaskViewFilter on TaskViewFilter {\n  type\n  tagIds\n  roleIds\n  ownerIds\n  assigneeIds\n  applicantIds\n  statuses\n  priorities\n  skillIds\n  subtasks\n  templateIds\n  organizationIds\n  __typename\n}\n\nfragment TaskViewSortBy on TaskViewSortBy {\n  field\n  direction\n  __typename\n}\n\nfragment FundingSession on FundingSession {\n  id\n  startDate\n  endDate\n  closedAt\n  amount\n  permalink\n  organizationId\n  token {\n    ...PaymentToken\n    network {\n      ...PaymentNetwork\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GraphNode on GraphNode {\n  id\n  type\n  name\n  icon\n  imageUrl\n  createdAt\n  permalink\n  __typename\n}\n"
})
headers = {
  'content-type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# grab the json object which contains the workspace id's
dework_workspaces = json.loads(response.text)["data"]["organization"]["workspaces"]

# extract the workspace id's from dework request
wspace_list = []
for team in dework_workspaces:
  wspace_list.append(team["id"])

# save all json objects with details for each workspace
for workspace_id in wspace_list:
  payload = json.dumps({
    "operationName": "GetWorkspaceTasksQuery",
    "variables": {
      "workspaceId": workspace_id
    },
    "query": "query GetWorkspaceTasksQuery($workspaceId: UUID!) {\n  workspace: getWorkspace(id: $workspaceId) {\n    id\n    tasks {\n      ...Task\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Task on Task {\n  id\n  name\n  description\n  status\n  priority\n  sortKey\n  storyPoints\n  dueDate\n  createdAt\n  doneAt\n  deletedAt\n  template\n  templateTaskId\n  templateTask {\n    id\n    name\n    __typename\n  }\n  workspaceId\n  workspace {\n    ...Workspace\n    __typename\n  }\n  parentTaskId\n  parentTask {\n    id\n    name\n    __typename\n  }\n  sectionId\n  number\n  gating\n  openToBids\n  submissionCount\n  applicationCount\n  subtasks {\n    ...Subtask\n    __typename\n  }\n  tags {\n    ...TaskTag\n    __typename\n  }\n  skills {\n    ...Skill\n    __typename\n  }\n  assignees {\n    ...User\n    __typename\n  }\n  owners {\n    ...User\n    __typename\n  }\n  creator {\n    ...User\n    __typename\n  }\n  rewards {\n    ...TaskReward\n    __typename\n  }\n  review {\n    ...TaskReview\n    __typename\n  }\n  reactions {\n    ...TaskReaction\n    __typename\n  }\n  __typename\n}\n\nfragment TaskTag on TaskTag {\n  id\n  label\n  color\n  createdAt\n  deletedAt\n  workspaceId\n  __typename\n}\n\nfragment Skill on Skill {\n  id\n  name\n  emoji\n  imageUrl\n  __typename\n}\n\nfragment TaskReward on TaskReward {\n  id\n  amount\n  peggedToUsd\n  fundingSessionId\n  token {\n    ...PaymentToken\n    network {\n      ...PaymentNetwork\n      __typename\n    }\n    __typename\n  }\n  tokenId\n  payments {\n    id\n    amount\n    user {\n      ...User\n      __typename\n    }\n    payment {\n      ...Payment\n      __typename\n    }\n    __typename\n  }\n  count\n  type\n  __typename\n}\n\nfragment Payment on Payment {\n  id\n  status\n  data\n  paymentMethod {\n    ...PaymentMethod\n    __typename\n  }\n  __typename\n}\n\nfragment PaymentMethod on PaymentMethod {\n  id\n  type\n  address\n  network {\n    ...PaymentNetwork\n    __typename\n  }\n  __typename\n}\n\nfragment PaymentNetwork on PaymentNetwork {\n  id\n  slug\n  name\n  type\n  config\n  sortKey\n  __typename\n}\n\nfragment PaymentToken on PaymentToken {\n  id\n  exp\n  type\n  name\n  symbol\n  address\n  identifier\n  usdPrice\n  networkId\n  visibility\n  imageUrl\n  __typename\n}\n\nfragment User on User {\n  id\n  username\n  imageUrl\n  permalink\n  nodeId\n  __typename\n}\n\nfragment Subtask on Task {\n  id\n  name\n  status\n  sortKey\n  __typename\n}\n\nfragment TaskReview on TaskReview {\n  id\n  message\n  rating\n  createdAt\n  __typename\n}\n\nfragment TaskReaction on TaskReaction {\n  id\n  userId\n  reaction\n  __typename\n}\n\nfragment Workspace on Workspace {\n  id\n  slug\n  name\n  icon\n  type\n  status\n  description\n  startAt\n  endAt\n  deletedAt\n  organizationId\n  permalink\n  sectionId\n  parentId\n  sortKey\n  roadmapSortKey\n  options {\n    showCommunitySuggestions\n    __typename\n  }\n  __typename\n}\n"
  })
  headers = {
    'content-type': 'application/json'
  }

  response2 = requests.request("POST", url, headers=headers, data=payload)
  output_json = "./json/"+workspace_id+".json"
  with open(output_json, "w+") as f:
    json.dump(json.loads(response2.text), f, indent=2)